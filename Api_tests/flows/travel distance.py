"""
do the steps for the following cases:
actual distance less than quarter of estimated distance
actual distance greater than quarter of estimated distance
actual distance is null

the verification is done through Grafana logs
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
preconditions:
1 - idle driver
2 - driver is at store location
3 - set url service names in API data file
4 - set super admin credentials in API data file
5 - set store name in API data file
6 - set store coordinates in API data file
7 - has no other drivers available
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
driver_username = input("please insert driver username: ") or "catN"
driver_password = input("please insert driver password: ") or "testTest1!"
driver_numeric_id = input("please insert driver id: ") or 31
store_id_string = input("please insert store name: ") or ApiData.dark_store
store_id_numeric = input("please insert store id: ") or 5
store_latitude = input("please insert store latitude: ") or ApiData.store_lat
store_longitude = input("please insert store longitude: ") or ApiData.store_long
locations = [33.70, 44.70]
required_actual_distance = int(input(
    "please check the required actual distance value: \n 1. null\n 2. less than quarter\n 3. more than quarter\nenter "
    "your choice: "))


# -------------------------------------------
# functions to be used in the script
def update_store_settings(token, store_id):
    response = DarkStoreApis.api_update_store_settings(token, store_id, {
        "max_threshold_waiting_time": 0,
        "max_orders_assigned": 3,
        "email_address": "update-store@gmail.com",
        "max_distance_from_dark_store": 200,
        "score_divisor": 1,
        "interval_time": 30,
        "interval_weight": 2,
        "stop_auto_assignment": True,
        "stop_auto_clock_out": True,
        "delivered_orders_count_weight": 0.5,
        "delivered_orders_distance_weight": 0.3,
        "waiting_time_at_the_darkstore_weight": 0.2
    })
    assert response.status_code == 200, print("can't update store settings " + response.json())


def create_order(order_name, store_id):
    response = OrderApis.api_create_auto_assignment_order(order_name, store_id)
    assert response.status_code == 200, print(response.json())
    order_id = response.json()['data']['id']
    print("order with id: " + str(order_id) + " has been created successfully.")
    return order_id


def ready_for_pickup(order_id):
    response = OrderApis.set_ready_for_pickup_status(order_id)
    assert response.status_code == 200, print(response.json())


def manually_assign_order(token, order_id, driver_id):
    response = OrderApis.assign_order_manually(token, order_id[0], payload_dict={
        "driver_id": driver_id,
        "order_sequence": order_id,
        "reason_id": 0,
        "note": "string"
    })
    assert response.status_code == 200, print(response.json())


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


def get_order_details(token, order_id):
    response = OrderApis.api_get_order_by_id(order_id, token)
    assert response.status_code == 200, print(response.json())
    # return response.json()['data']['traveled_distance']
    return response.json()


def deliver_order(driver_token, order_id):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_token
    }
    url = environment_url + "/order/order_delivered/" + str(order_id)
    response = requests.request("PUT", url, headers=headers)
    assert response.status_code == 200, print("can't deliver order " + response.json())


# ------------------------------------------------------------------------------------------------
# flow starts:
# login with admin
admin_access_token = login(ApiData.superadmin_username, ApiData.superadmin_password)
# update store settings
update_store_settings(token=admin_access_token, store_id=store_id_numeric)
# create order and assign it manually
order_id = create_order(order_name=order_id_string + "0", store_id=store_id_string)
ready_for_pickup(order_id)
manually_assign_order(token=admin_access_token, order_id=[order_id], driver_id=driver_numeric_id)
# pick orders up
pick_up_order(order_id, admin_access_token)
# login with driver
driver_access_token = login(driver_username, driver_password)
# change driver status to outward
print("waiting for system to allow moving outward...")
status: int
for x in range(20):
    status = update_driver_status(driver_access_token, driver_numeric_id, order_id, 6)
    if status == 200:
        break
    time.sleep(6)
assert status == 200, print(status)
print("driver now is on the way")
estimated_distance = get_order_details(admin_access_token, order_id)['data']['trip_details_from_darkstore_outward'][
    'travel_distance']
print("estimated distance is " + str(estimated_distance))
# set location
if required_actual_distance == 1:
    print("no location has been set during the trip")
elif required_actual_distance == 2:
    location_distance = (int(estimated_distance) / 4) - 100
    set_location(driver_token=driver_access_token, latitude=locations[0], longitude=locations[1],
                 distance=location_distance)
    print("location distance is " + str(location_distance))
elif required_actual_distance == 3:
    location_distance = (int(estimated_distance) / 4) + 100
    set_location(driver_token=driver_access_token, latitude=locations[0], longitude=locations[1],
                 distance=location_distance)
    print("location distance is " + str(location_distance))
else:
    print("invalid option value is selected for required actual distance: " + str(required_actual_distance))

# driver at address
status = update_driver_status(driver_access_token, driver_numeric_id, order_id, 7)
assert status == 200, print(status)
print("driver is at address")
# deliver order
deliver_order(driver_token=driver_access_token, order_id=order_id)
print("order is delivered successfully")
time.sleep(65)
# set driver location at store
if required_actual_distance != 1:
    set_location(driver_access_token, store_latitude, store_longitude, 10)
# set driver idle
status = update_driver_status(driver_access_token, driver_numeric_id, 0, 3)
assert status == 200, print(status)
print("driver is at store")
# verify order traveled distance
order_details = get_order_details(admin_access_token, order_id)
print("traveled distance is " + str(order_details['data']['traveled_distance']))
