"""
this script helps in testing automatic assignment in distribute mode
it makes sure that system switch to fairness score properly
it makes sure that only idle drivers are included in the fairness calculations
it makes sure that the driver with the highest score is assigned to the order
it makes sure that the order is assigned to the driver with the oldest first assignment
it makes sure that the order is assigned to the driver with the lowest number of assigned orders
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

"""
gathering required information from user
"""
environment_url = ApiData.api_url
file_handler = open("order_latest_name.txt", "r")
file_content = file_handler.read()
print("the latest order name used was " + file_content)
order_id_string = input("please add new order name: ")
file_handler.close()
file_handler = open("order_latest_name.txt", "w")
file_handler.write(order_id_string)
file_handler.close()
darkstore_id_string = input("please insert store name: ") or "DSBGR008-Al-Qahira - TG"
darkstore_id_numeric = input("please insert store id: ") or 5
vehicle_type_id = input("please insert vehicle type id: ") or 2

"""
don't make any changes in  the following lines:
"""
first_order_id: int
first_assigned_driver: int


# -------------------------------------------
# functions to be used in the script
def update_store_settings(token, store_id, stop_auto_assignment_flag):
    response = DarkStoreApis.api_update_store_settings(token, store_id, {
        "max_threshold_waiting_time": 3600,
        "max_orders_assigned": 3,
        "email_address": "update-store@gmail.com",
        "max_distance_from_dark_store": 200,
        "score_divisor": 2,
        "interval_time": 90,
        "interval_weight": 2,
        "stop_auto_assignment": stop_auto_assignment_flag,
        "stop_auto_clock_out": True,
        "delivered_orders_count_weight": 0.5,
        "delivered_orders_distance_weight": 0.3,
        "waiting_time_at_the_darkstore_weight": 0.2
    })
    assert response.status_code == 200, print(response)


def create_order(order_name, store_id):
    response = OrderApis.api_create_auto_assignment_order(order_name, store_id)
    assert response.status_code == 200, print(response)
    order_id = response.json()['data']['id']
    print("order with id: " + str(order_id) + " has been created successfully.")
    return order_id


def get_scores(token, store_id, vehicle_id):
    scores_dict = {}
    response = DriverEndPoints.api_get_fairness_scores(token, store_id, vehicle_id)
    assert response.status_code == 200, print(response)
    for x in response.json()['data']['page_records']:
        if x['fairness_score'] is not None:
            scores_dict[x['driver']['id']] = x['fairness_score']
    return scores_dict


def ready_for_pickup(order_id):
    response = OrderApis.set_ready_for_pickup_status(order_id)
    assert response.status_code == 200, print(response)
    print("order is ready for pickup")


def get_order_driver_id(token, order_id):
    response = OrderApis.api_get_order_by_id(order_id, token)
    assert response.status_code == 200, print(response)
    assigned_driver = response.json()['data']['driver_id']
    print("the assigned driver is: " + str(assigned_driver))
    return assigned_driver


def check_exclusion(token, store_id, vehicle_id, driver_id):
    response = DriverEndPoints.api_get_fairness_scores(token, store_id, vehicle_id)
    assert response.status_code == 200, print(response)
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
    assert response.status_code == 200, print(response)
    print("order " + str(order_ids[0]) + " has been assigned manually successfully to driver " + str(driver_id))


def cancel_order(token, order_id):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    payload = json.dumps({

        "order_status_id": 12
    })
    url = environment_url + "/order/update_order_status_internally/" + str(order_id)
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response


# login with admin
response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
assert response.status_code == 200, print(response)
admin_access_token = response.json()['data']['access_token']
# update store settings
update_store_settings(token=admin_access_token, store_id=darkstore_id_numeric, stop_auto_assignment_flag=False)
# create order first order
first_order_id = create_order(order_name=order_id_string + "0", store_id=darkstore_id_string)
# get fairness scores
scores_dict = get_scores(admin_access_token, darkstore_id_numeric, vehicle_type_id)
print("scores of the available drivers are: " + str(scores_dict))
# move order status to ready for pickup
ready_for_pickup(first_order_id)
# check who is assigned
print("waiting for automatic assignment...")
for x in range(10):
    if OrderApis.api_get_order_by_id(first_order_id, admin_access_token).json()['data']['driver_id']:
        break
    time.sleep(5)
first_assigned_driver = get_order_driver_id(admin_access_token, first_order_id)
# verify if the driver with the highest score is assigned
verify_assignment(first_assigned_driver, scores_dict)
# verify that idle_assigned driver has been excluded
print("waiting for assigned driver exclusion...")
time.sleep(50)
check_exclusion(admin_access_token, darkstore_id_numeric, vehicle_type_id, first_assigned_driver)
# create second order
second_order_id = create_order(order_id_string + "1", darkstore_id_string)
# get fairness score
scores_dict = get_scores(admin_access_token, darkstore_id_numeric, vehicle_type_id)
print("scores of the available drivers are: " + str(scores_dict))
# move order status to ready for pickup
ready_for_pickup(second_order_id)
# check who is assigned
print("waiting for automatic assignment...")
for x in range(10):
    if OrderApis.api_get_order_by_id(second_order_id, admin_access_token).json()['data']['driver_id']:
        break
    time.sleep(5)
second_assigned_driver = get_order_driver_id(admin_access_token, second_order_id)
# verify if the driver with the highest score is assigned
verify_assignment(second_assigned_driver, scores_dict)
# verify that idle_assigned driver has been excluded
print("waiting for assigned driver exclusion...")
time.sleep(50)
check_exclusion(admin_access_token, darkstore_id_numeric, vehicle_type_id, second_assigned_driver)
# create third order
third_order_id = create_order(order_id_string + "2", darkstore_id_string)
# get fairness score
scores_dict = get_scores(admin_access_token, darkstore_id_numeric, vehicle_type_id)
print("scores of the available drivers are: " + str(scores_dict))
# move order status to ready for pickup
ready_for_pickup(third_order_id)
# check who is assigned
print("waiting for automatic assignment...")
for x in range(10):
    if OrderApis.api_get_order_by_id(third_order_id, admin_access_token).json()['data']['driver_id']:
        break
    time.sleep(5)
third_assigned_driver = get_order_driver_id(admin_access_token, third_order_id)
# verify if the driver with the highest score is assigned
verify_assignment(third_assigned_driver, scores_dict)
# verify that idle_assigned driver has been excluded
print("waiting for assigned driver exclusion...")
time.sleep(50)
check_exclusion(admin_access_token, darkstore_id_numeric, vehicle_type_id, third_assigned_driver)
# create fourth order
fourth_order_id = create_order(order_id_string + "3", darkstore_id_string)
# move order status to ready for pickup
ready_for_pickup(fourth_order_id)
# check who is assigned
print("waiting for automatic assignment...")
for x in range(10):
    if OrderApis.api_get_order_by_id(fourth_order_id, admin_access_token).json()['data']['driver_id']:
        break
    time.sleep(5)
assigned_driver = get_order_driver_id(admin_access_token, fourth_order_id)
# verify that driver with the oldest assignment is assigned
assert assigned_driver == first_assigned_driver, print(assigned_driver)
print("driver driver with oldest first_assignment has been assigned successfully")
# cancel_third_order
response = cancel_order(admin_access_token, third_order_id)
assert response.status_code == 200, print(response)
print(str(third_order_id) + " has been canceled successfully")
# clock_out_third_assigned_driver
response = DriverEndPoints.api_force_clock_out(admin_access_token, third_assigned_driver)
assert response.status_code == 200, print(response)
# disable auto-assignment
update_store_settings(token=admin_access_token, store_id=darkstore_id_numeric, stop_auto_assignment_flag=True)
# create fifth order
fifth_order_id = create_order(order_id_string + "4", darkstore_id_string)
# move order status to ready for pickup
ready_for_pickup(fifth_order_id)
# assign order manually to second assigned driver
manually_assign_order(token=admin_access_token, order_ids=[fifth_order_id, second_order_id],
                      driver_id=second_assigned_driver)
# create sixth order
sixth_order_id = create_order(order_id_string + "5", darkstore_id_string)
# move order status to ready for pickup
ready_for_pickup(sixth_order_id)
# assign order manually to first assigned driver
manually_assign_order(token=admin_access_token, order_ids=[sixth_order_id, first_order_id, fourth_order_id],
                      driver_id=first_assigned_driver)
# enable auto-assignment
update_store_settings(token=admin_access_token, store_id=darkstore_id_numeric, stop_auto_assignment_flag=False)
# create seventh order
seventh_order_id = create_order(order_id_string + "6", darkstore_id_string)
# move order status to ready for pickup
ready_for_pickup(seventh_order_id)
# check who is assigned
print("waiting for automatic assignment...")
for x in range(10):
    if OrderApis.api_get_order_by_id(seventh_order_id, admin_access_token).json()['data']['driver_id']:
        break
    time.sleep(5)
final_assigned_driver = get_order_driver_id(admin_access_token, seventh_order_id)
# verify if the driver with the lowest number of assigned orders
assert final_assigned_driver == second_assigned_driver, print(final_assigned_driver)
print("seventh order has been assigned to the driver with the lowest number of assigned orders")
