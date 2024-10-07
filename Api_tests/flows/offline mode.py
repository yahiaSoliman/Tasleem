"""
the script is verifying that system record locations visited by driver in offline mode
the steps are as following:
- create order
- assign order
- outward
- record two locations
- record Batch of locations
- deliver order
- verify traveled distance

preconditions:
1 - idle driver
2 - driver is at store location
"""

import json
import time
from datetime import datetime

import pytz
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
store_id_string = input("please insert store name: ") or "DSBGR008-Al-Qahira - TG"
store_id_numeric = input("please insert store id: ") or 5
store_latitude = input("please insert store latitude: ") or ApiData.store_lat
store_longitude = input("please insert store longitude: ") or ApiData.store_long
locations = [33.50, 44.50, 33.60, 44.60, 33.70, 44.70, 33.80, 44.80]


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


def manually_assign_order(token, order_id, driver_id):
    response = OrderApis.assign_order_manually(token, order_id[0], payload_dict={
        "driver_id": driver_id,
        "order_sequence": order_id,
        "reason_id": 0,
        "note": "string"
    })
    assert response.status_code == 200, print(response.json())
    print("order " + str(order_id[0]) + " has been assigned manually successfully to driver " + str(driver_id))


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


def login(username, password):
    response = AuthEndPoints.api_login(username, password)
    assert response.status_code == 200, print("can't login")
    return response.json()['data']['access_token']


def set_location(driver_token, latitude, longitude, distance):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_token
    }
    dateInBaghdad = str(datetime.now(pytz.timezone('Asia/Baghdad')).date())
    timeInBaghdad = str(datetime.now(pytz.timezone('Asia/Baghdad')).time())[0:8]
    payload = json.dumps({
        "latitude": latitude,
        "longitude": longitude,
        "distance": distance,
        "speed": "60",
        "accuracy": "10",
        "timestamp": dateInBaghdad + "T" + timeInBaghdad
    })
    url = ApiData.location_api_url + "/location/"
    response = requests.request("POST", url, data=payload, headers=headers)
    assert response.status_code == 200, print(response.json())


def set_batch_of_locations(driver_token, distance, batch_locations):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_token
    }
    dateInBaghdad_1 = str(datetime.now(pytz.timezone('Asia/Baghdad')).date())
    timeInBaghdad_1 = str(datetime.now(pytz.timezone('Asia/Baghdad')).time())[0:5]
    time.sleep(65)
    dateInBaghdad_2 = str(datetime.now(pytz.timezone('Asia/Baghdad')).date())
    timeInBaghdad_2 = str(datetime.now(pytz.timezone('Asia/Baghdad')).time())[0:5]
    payload = json.dumps({
        "locations": [
            {
                "latitude": batch_locations[0],
                "longitude": batch_locations[1],
                "distance": distance,
                "speed": "60",
                "accuracy": "10",
                "timestamp": dateInBaghdad_1 + "T" + timeInBaghdad_1 + ":00"
            },
            {
                "latitude": batch_locations[2],
                "longitude": batch_locations[3],
                "distance": distance,
                "speed": "60",
                "accuracy": "10",
                "timestamp": dateInBaghdad_2 + "T" + timeInBaghdad_2 + ":00"
            }
        ]
    })
    url = ApiData.location_api_url + "/location/batch_location"
    response = requests.request("POST", url, data=payload, headers=headers)
    assert response.status_code == 200, print(response.json())


def get_traveled_distance(token, order_id):
    response = OrderApis.api_get_order_by_id(order_id, token)
    assert response.status_code == 200, print(response.json())
    return response.json()['data']['traveled_distance']


def deliver_order(driver_token, order_id):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_token
    }
    url = environment_url + "/order/order_delivered/" + str(order_id)
    response = requests.request("PUT", url, headers=headers)
    assert response.status_code == 200, print("can't deliver order")


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
ready_for_pickup(order_id_a)
manually_assign_order(token=admin_access_token, order_id=[order_id_a], driver_id=driver_numeric_id)
# pick orders up
pick_up_order(order_id_a, admin_access_token)
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
# set locations in online mode
set_location(driver_token=driver_access_token, latitude=locations[0], longitude=locations[1], distance=20)
time.sleep(65)
set_location(driver_token=driver_access_token, latitude=locations[2], longitude=locations[3], distance=20)
time.sleep(65)
# set batch of locations
time.sleep(65)
set_batch_of_locations(driver_token=driver_access_token, distance=50, batch_locations=locations[4:])
# deliver the order
status = update_driver_status(driver_access_token, driver_numeric_id, order_id_a, 7)
assert status == 200, print(status)
print("driver is at address")
# deliver order
deliver_order(driver_token=driver_access_token, order_id=order_id_a)
print("order is delivered successfully")
time.sleep(65)
# set driver location at store
set_location(driver_access_token, store_latitude, store_longitude, 10)
# set driver idle
status = update_driver_status(driver_access_token, driver_numeric_id, 0, 3)
assert status == 200, print(status)
print("driver is at store")
# verify order traveled distance
traveled_distance = get_traveled_distance(admin_access_token, order_id_a)
print("traveled distance is " + str(traveled_distance) + " and the expected result is 140")
