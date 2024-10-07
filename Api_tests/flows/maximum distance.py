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
2 - at store
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
location_lat = input("please insert far location latitude: ") or 33.39055633544922
location_long = input("please insert far location longitude: ") or 44.37400109863281
in_location_lat = input("please insert close location latitude: ") or 33.39055633544922
in_location_long = input("please insert close location longitude: ") or 44.37320010986328
maximum_distance = input("please insert maximum distance: ") or 80


# -------------------------------------------
# functions to be used in the script
def update_store_settings(token, store_id):
    response = DarkStoreApis.api_update_store_settings(token, store_id, {
        "max_threshold_waiting_time": 0,
        "max_orders_assigned": 3,
        "email_address": "update-store@gmail.com",
        "max_distance_from_dark_store": maximum_distance,
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
    return response


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
# create order
order_id = create_order(order_name=order_id_string + "0", store_id=store_id_string)
ready_for_pickup(order_id)
manually_assign_order(token=admin_access_token, order_ids=[order_id], driver_id=driver_numeric_id)
# pick orders up
pick_up_order(order_id, admin_access_token)
print("order has been picked up successfully")
# login with driver
driver_access_token = login(driver_username, driver_password)
# change driver status to outward
print("waiting for system to allow moving outward...")
status = ""
for x in range(20):
    status = int(update_driver_status(driver_access_token, driver_numeric_id, order_id, 6).status_code)
    if status == 200:
        break
    time.sleep(6)
assert status == 200, print(status)
print("driver now is on the way")
# deliver the order
status = int(update_driver_status(driver_access_token, driver_numeric_id, order_id, 7).status_code)
assert status == 200, print(status)
print("driver is at address")
# deliver order
deliver_order(driver_token=driver_access_token, order_id=order_id)
print("order has been delivered successfully")
# set driver location far from store
set_location(driver_access_token, location_lat, location_long, 20)
print("now driver location is far from store")
# change driver status to be AT Store
response = update_driver_status(driver_access_token, driver_numeric_id, 0, 3)
assert response.status_code == 400, print(response.json())
assert str(response.json()["info"][
               "message"]).__contains__("You cannot change status because you are not at the dark store yet")
print("negative scenario passed")
# set driver location close to store
set_location(driver_access_token, in_location_lat, in_location_long, 20)
print("now driver location is close to store")
# change driver status to be AT Store
response = update_driver_status(driver_access_token, driver_numeric_id, 0, 3)
assert response.status_code == 200, print(response.json())
assert str(response.json()["info"]["message"]).__contains__("success")
print("positive scenario passed")
