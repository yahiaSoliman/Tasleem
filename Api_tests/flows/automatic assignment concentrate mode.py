"""
verify that system switch to fairness score if all available drivers are idle
verify that system keep assigning to the same driver until getting the maximum assigned orders count
verify that driver is excluded when assigned to the maximum assigned orders count
verify that system assign to the driver with the highest number of assigned orders
"""
import json
import time

import requests

from API.auth_api import AuthEndPoints
from API.darkstore_api import DarkStoreApis
from API.driver_api import DriverEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData

"""
preconditions are:
1- have 3 idle drivers in your store
"""

file_handler = open("order_latest_name.txt", "r")
file_content = file_handler.read()
print("the latest order name used was " + file_content)
order_id_string = input("please add new order name: ")
file_handler.close()
file_handler = open("order_latest_name.txt", "w")
file_handler.write(order_id_string)
file_handler.close()

darkstore_id_string = ApiData.dark_store
darkstore_id_numeric = input("please insert store id: ") or 5
vehicle_type_id = input("please insert vehicle type id: ") or 2


# -------------------------------------------
# functions to be used in the script
def update_store_settings(token, store_id, stop_auto_assignment_flag, maximum_orders):
    response = DarkStoreApis.api_update_store_settings(token, store_id, {
        "max_threshold_waiting_time": 3600,
        "max_orders_assigned": maximum_orders,
        "email_address": "update-store@gmail.com",
        "max_distance_from_dark_store": 80,
        "score_divisor": 1,
        "interval_time": 30,
        "interval_weight": 2,
        "stop_auto_assignment": stop_auto_assignment_flag,
        "stop_auto_clock_out": True,
        "delivered_orders_count_weight": 0.5,
        "delivered_orders_distance_weight": 0.3,
        "waiting_time_at_the_darkstore_weight": 0.2
    })
    assert response.status_code == 200, "can't update store settings"


def create_order(order_name, store_id):
    response = OrderApis.api_create_auto_assignment_order(order_name, store_id)
    assert response.status_code == 200, "can't create order"
    order_id = response.json()['data']['id']
    print("order with id: " + str(order_id) + " has been created successfully.")
    return order_id


def get_scores(token, store_id, vehicle_id):
    scores_dict = {}
    response = DriverEndPoints.api_get_fairness_scores(token, store_id, vehicle_id)
    assert response.status_code == 200, "can't get fairness scores"
    for x in response.json()['data']['page_records']:
        if x['fairness_score'] is not None:
            scores_dict[x['driver']['id']] = x['fairness_score']
    return scores_dict


def ready_for_pickup(order_id):
    response = OrderApis.set_ready_for_pickup_status(order_id)
    assert response.status_code == 200, "can't set order ready for pickup"
    print("order is ready for pickup")


def get_order_details(token, order_id):
    response = OrderApis.api_get_order_by_id(order_id, token)
    assert response.status_code == 200, "can't get order details"
    assigned_driver = response.json()['data']['driver_id']
    print("the assigned driver is: " + str(assigned_driver))
    return assigned_driver


def check_exclusion(token, store_id, vehicle_id, driver_id):
    response = DriverEndPoints.api_get_fairness_scores(token, store_id, vehicle_id)
    assert response.status_code == 200, "can't get fairness scores"
    for x in response.json()['data']['page_records']:
        if x['driver']['id'] == driver_id:
            assert x['fairness_score'] is None, "assigned driver has not been excluded from available ones"
    print("idle_assigned driver has been excluded successfully")


def verify_assignment(driver_id, scores):
    assert driver_id == max(scores, key=scores.get), "invalid driver is assigned: " + str(
        driver_id)
    print("driver with the highest score has been assigned successfully")


def manually_assign_order(token, order_ids, driver_id):
    response = OrderApis.assign_order_manually(token, order_ids[0], payload_dict={
        "driver_id": driver_id,
        "order_sequence": order_ids,
        "reason_id": 0,
        "note": "string"
    })
    assert response.status_code == 200, "can't assign order manually"
    print("order " + str(order_ids[0]) + " has been assigned manually successfully to driver " + str(driver_id))


def cancel_order(token, order_id):
    global response
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    payload = json.dumps({

        "order_status_id": 12
    })
    url = ApiData.api_url + "/order/update_order_status_internally/" + str(order_id)
    response = requests.request("PUT", url, headers=headers, data=payload)

# ---------------------------------------------------------------------------------------------------------
# flow starts:
# login with admin
response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
assert response.status_code == 200, "can't login admin"
admin_access_token = response.json()['data']['access_token']
# update store settings
update_store_settings(token=admin_access_token, store_id=darkstore_id_numeric, stop_auto_assignment_flag=False,
                      maximum_orders=2)
print("maximum orders configuration is updated to be 2")
# create order first order
first_order_id = create_order(order_name=order_id_string + "0", store_id=darkstore_id_string)
# get fairness scores
scores_dict = get_scores(admin_access_token, darkstore_id_numeric, vehicle_type_id)
print("scores of the available drivers are: " + str(scores_dict))
# move order status to ready for pickup
ready_for_pickup(first_order_id)
# check who is assigned
print("waiting for automatic assignment...")
time.sleep(30)
first_assigned_driver = get_order_details(admin_access_token, first_order_id)
# verify if the driver with the highest score is assigned
verify_assignment(first_assigned_driver, scores_dict)
# verify that idle_assigned driver has been excluded
print("waiting for assigned driver exclusion...")
time.sleep(50)
check_exclusion(admin_access_token, darkstore_id_numeric, vehicle_type_id, first_assigned_driver)
# create second order
second_order_id = create_order(order_id_string + "1", darkstore_id_string)
# move order status to ready for pickup
ready_for_pickup(second_order_id)
# check who is assigned
print("waiting for automatic assignment...")
time.sleep(30)
assert first_assigned_driver == get_order_details(admin_access_token, second_order_id)
print("order has been assigned to the idle_assigned driver " + str(first_assigned_driver) + " successfully")
# create third order
third_order_id = create_order(order_name=order_id_string + "2", store_id=darkstore_id_string)
# get fairness scores
scores_dict = get_scores(admin_access_token, darkstore_id_numeric, vehicle_type_id)
print("scores of the available drivers are: " + str(scores_dict))
# move order status to ready for pickup
ready_for_pickup(third_order_id)
# check who is assigned
print("waiting for automatic assignment...")
time.sleep(90)
second_assigned_driver = get_order_details(admin_access_token, third_order_id)
# verify if the driver with the highest score is assigned
verify_assignment(second_assigned_driver, scores_dict)
print("system switched to fairness score again successfully")
# update store settings
update_store_settings(token=admin_access_token, store_id=darkstore_id_numeric, stop_auto_assignment_flag=True,
                      maximum_orders=3)
print("auto-assignment has been disabled")
# cancel_orders
cancel_order(admin_access_token, first_order_id)
cancel_order(admin_access_token, second_order_id)
cancel_order(admin_access_token, third_order_id)
print("all orders have been canceled")
# create two orders and assign them manually to the first driver
order_id_a = create_order(order_name=order_id_string + "3", store_id=darkstore_id_string)
order_id_b = create_order(order_name=order_id_string + "4", store_id=darkstore_id_string)
ready_for_pickup(order_id_a)
ready_for_pickup(order_id_b)
manually_assign_order(token=admin_access_token, order_ids=[order_id_a], driver_id=first_assigned_driver)
manually_assign_order(token=admin_access_token, order_ids=[order_id_b, order_id_a], driver_id=first_assigned_driver)
print("two orders is manually assigned successfully to: " + str(first_assigned_driver))
# create one order and assign it manually to the second driver
order_id_c = create_order(order_name=order_id_string + "5", store_id=darkstore_id_string)
ready_for_pickup(order_id_c)
manually_assign_order(token=admin_access_token, order_ids=[order_id_c], driver_id=second_assigned_driver)
print("one order is manually assigned successfully to: " + str(second_assigned_driver))
# update store settings
update_store_settings(token=admin_access_token, store_id=darkstore_id_numeric, stop_auto_assignment_flag=False,
                      maximum_orders=3)
print("maximum orders configuration is updated to be 3")
print("auto-assignment has been enabled")
# create order
order_id = create_order(order_name=order_id_string + "6", store_id=darkstore_id_string)
# get fairness scores
scores_dict = get_scores(admin_access_token, darkstore_id_numeric, vehicle_type_id)
print("scores of the available drivers are: " + str(scores_dict))
# move order status to ready for pickup
ready_for_pickup(order_id)
# check who is assigned
print("waiting for automatic assignment...")
time.sleep(30)
assigned_driver = get_order_details(admin_access_token, order_id)
# verify if the assigned driver is the one with the highest number of assigned orders
assert assigned_driver == first_assigned_driver, "invalid driver has been assigned"
print("order has been assigned to the driver with the highest number of assigned order")
