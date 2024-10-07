"""
delivery flow for 2 orders per driver with one unable to deliver order
verify that the other order can be delivered successfully
verify the status of unable-to-deliver order
verify if unable-to-deliver order is still linked to the driver
"""
from datetime import datetime

import pytz

"""
preconditions are:
1- have 1 idle drivers in your store
"""

import json
import time
import requests
from API.auth_api import AuthEndPoints
from API.darkstore_api import DarkStoreApis
from API.order_api import OrderApis
from core.api_data import ApiData

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
driver_username = input("please insert driver username: ") or "catN"
driver_password = input("please insert driver password: ") or "testTest1!"
driver_numeric_id = input("please insert driver id: ") or 31
store_id_string = input("please insert store name: ") or ApiData.dark_store
store_id_numeric = input("please insert store id: ") or 5
store_latitude = input("please insert store latitude: ") or ApiData.store_lat
store_longitude = input("please insert store longitude: ") or ApiData.store_long


# -------------------------------------------
# functions to be used in the script
def update_store_settings(token, store_id, stop_auto_assignment_flag):
    response = DarkStoreApis.api_update_store_settings(token, store_id, {
        "max_threshold_waiting_time": 0,
        "max_orders_assigned": 3,
        "email_address": "update-store@gmail.com",
        "max_distance_from_dark_store": 200,
        "score_divisor": 1,
        "interval_time": 30,
        "interval_weight": 2,
        "stop_auto_assignment": stop_auto_assignment_flag,
        "stop_auto_clock_out": True,
        "delivered_orders_count_weight": 0.5,
        "delivered_orders_distance_weight": 0.3,
        "waiting_time_at_the_darkstore_weight": 0.2
    })
    assert response.status_code == 200, print("can't update store settings")


def create_order(order_name, store_id):
    response = OrderApis.api_create_auto_assignment_order(order_name, store_id)
    assert response.status_code == 200, print(response.json())
    order_id = response.json()['data']['id']
    print("order with id: " + str(order_id) + " has been created successfully.")
    return order_id


def ready_for_pickup(order_id):
    response = OrderApis.set_ready_for_pickup_status(order_id)
    assert response.status_code == 200, print(response.json())
    print("order is ready for pickup")


def get_order_status(token, order_id):
    response = OrderApis.api_get_order_by_id(order_id, token)
    assert response.status_code == 200, print(response.json())
    status_name = response.json()['data']['order_status']['name']
    return status_name


def manually_assign_order(token, order_ids, driver_id):
    response = OrderApis.assign_order_manually(token, order_ids[0], payload_dict={
        "driver_id": driver_id,
        "order_sequence": order_ids,
        "reason_id": 0,
        "note": "string"
    })
    assert response.status_code == 200, print(response.json())
    print("order " + str(order_ids[0]) + " has been assigned manually successfully to driver " + str(driver_id))


def pick_up_order(order_id, token):
    payload = json.dumps({
        "order_status_id": 4
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url_order_status = environment_url + "/order/update_order_status/" + str(order_id)
    response = requests.request("PUT", url_order_status, headers=headers, data=payload)
    assert response.status_code == 200, print(response.json())
    print("order " + str(order_id) + " has been picked up successfully")


def update_driver_status(token, driver_id, order_id, driver_status_id):
    payload = json.dumps({
        "driver_status_id": driver_status_id,
        "order_id": order_id
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url = environment_url + "/drivers/update_driver_status/" + str(driver_id)
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.status_code


def unable_to_deliver_order(token, driver_id, order_id):
    payload = json.dumps({
        "reason_id": 1,
        "order_id": order_id
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url = environment_url + "/drivers/unable_to_deliver/" + str(driver_id)
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200, print(response.json())
    print("order " + str(order_id) + " has been set as Unable-To-Deliver")


def login(username, password):
    response = AuthEndPoints.api_login(username, password)
    assert response.status_code == 200, print("can't login")
    return response.json()['data']['access_token']


def driver_orders(driver_token, driver_id):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_token
    }
    url = environment_url + "/drivers/driver_orders/" + str(driver_id)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200, print(response.status_code)
    return response.json()['data']['orders_sequence']


def deliver_order(driver_token, order_id):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_token
    }
    url = environment_url + "/order/order_delivered/" + str(order_id)
    response = requests.request("PUT", url, headers=headers)
    assert response.status_code == 200, print("can't deliver order")


def set_location(driver_token):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_token
    }
    dateInBaghdad = str(datetime.now(pytz.timezone('Asia/Baghdad')).date())
    timeInBaghdad = str(datetime.now(pytz.timezone('Asia/Baghdad')).time())[0:5]
    payload = json.dumps({
        "latitude": store_latitude,
        "longitude": store_longitude,
        "distance": "50",
        "speed": "60",
        "accuracy": "10",
        "timestamp": dateInBaghdad + "T" + timeInBaghdad + ":00"
    })
    url = ApiData.location_api_url + "/location/"
    response = requests.request("POST", url, data=payload, headers=headers)
    # assert response.status_code == 200, print(response.json())


# ------------------------------------------------------------------------------------------------
# flow starts:
# login with admin
response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
assert response.status_code == 200, "can't login admin"
admin_access_token = response.json()['data']['access_token']
# update store settings
update_store_settings(token=admin_access_token, store_id=store_id_numeric, stop_auto_assignment_flag=True)
# create two orders and assign them manually to the first driver
order_id_a = create_order(order_name=order_id_string + "0", store_id=store_id_string)
order_id_b = create_order(order_name=order_id_string + "1", store_id=store_id_string)
ready_for_pickup(order_id_a)
ready_for_pickup(order_id_b)
manually_assign_order(token=admin_access_token, order_ids=[order_id_a], driver_id=driver_numeric_id)
manually_assign_order(token=admin_access_token, order_ids=[order_id_b, order_id_a], driver_id=driver_numeric_id)
# pick orders up
pick_up_order(order_id_a, admin_access_token)
pick_up_order(order_id_b, admin_access_token)
# login with driver
driver_access_token = login(driver_username, driver_password)
# change driver status to outward
print("waiting for system to allow moving outward...")
status: int
for x in range(20):
    status = update_driver_status(driver_access_token, driver_numeric_id, order_id_a, 6)
    if status == 200:
        break
    time.sleep(6)
assert status == 200, print(status)
print("driver now is on the way")
# set order as Unable-To-Deliver
unable_to_deliver_order(driver_access_token, driver_numeric_id, order_id_a)
# verify the order status
time.sleep(30)
order_status = get_order_status(admin_access_token, order_id_a)
assert order_status == "to_return_assigned", print("order status is " + str(order_status))
print("order status has been updated successfully to to_return_assigned")
# verify order has been removed from driver orders list
time.sleep(30)
current_orders = driver_orders(driver_token=driver_access_token, driver_id=driver_numeric_id)
current_orders_length = len(current_orders)
assert current_orders_length == 1, print(
    "current orders of the driver is not valid, it is: " + str(current_orders_length))
current_order_id = current_orders[0]
assert current_order_id == order_id_b, print("current order id is not valid, it is: " + str(current_order_id))
print("the order has been removed from driver current orders list")
# deliver the remaining order
status = update_driver_status(driver_access_token, driver_numeric_id, order_id_b, 7)
assert status == 200, print(status)
print("driver is at address")
# deliver order
deliver_order(driver_token=driver_access_token, order_id=order_id_b)
print("remaining order has been delivered successfully")
# set driver location at store
set_location(driver_access_token)
# set driver idle
status = update_driver_status(driver_access_token, driver_numeric_id, 0, 3)
assert status == 200, print(status)
print("driver is at store")

