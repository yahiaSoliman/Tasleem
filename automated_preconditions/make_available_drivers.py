import json
import time
from datetime import datetime

import pytz
import requests

from API.auth_api import AuthEndPoints
from core.api_data import ApiData

"""
this script allow test to deliver order of each driver and each order
separately. so you can get the drivers available for your next test case.
the script can move the driver outward with multiple orders
the script can complete any interrupted trip 
if any steps are not needed it will be skipped automatically
"""
"""
driver statuses
###############
1 : idle
2 : idle_assigned
3 : at_the_darkstore
4 : occupied_inward
5 : occupied_inward_assigned
6 : occupied_outward
7 : at_the_address

order_statuses
##############
1 : preparing
2 : ready_for_pick_up
3 : assigned
4 : picked_up
5 : on_the_way
6 : at_the_address
7 : delivered
8 : to_return
9 : to_return_assigned
10: returned
11: delayed
12: canceled
"""

"""
preconditions:
1 -  maximum waiting time is zero
"""

environment_url = ApiData.api_url
admin_username = ApiData.superadmin_username
admin_password = ApiData.superadmin_password
latitude = input("please insert store latitude: ") or 33.39055633544922
longitude = input("please insert store longitude: ") or 44.37300109863281
store_id = input("please insert store id: ") or 1
driver_status = input("please insert driver status id: ") or 2
order_Status = input("please insert order status id: ") or 3
which_driver = 0

"""
functions to be used in the script
"""


def get_drivers(store_id, token, driver_status):
    parameters = {
        "page_number": 1,
        "per_page": 200,
        "dark_store_ids": store_id,
        "is_clocked_in": 1,
        "driver_status_ids": driver_status
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url_drivers = environment_url + "/drivers/page"
    response = requests.request("GET", url_drivers, headers=headers, params=parameters)
    return response


# ---------------------------------------------
def get_orders(token, driver_id, order_status):
    parameters = {
        "page_number": 1,
        "per_page": 10,
        "dark_store_ids": 1,
        "order_status_ids": order_status,
        "driver_ids": driver_id
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    url_orders = environment_url + "/order/page"
    return requests.request("GET", url_orders, headers=headers, params=parameters)


# --------------------------------------------
def pickup(order_status, admin_token, orders):
    global payload, headers, x, response, continue_flag
    payload = json.dumps({
        "order_status_id": order_status
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + admin_token
    }
    for x in range(len(orders)):
        url_order_status = environment_url + "/order/update_order_status/" + str(
            order_ids[x])
        response = requests.request("PUT", url_order_status, headers=headers, data=payload)
        if response.status_code == 200:
            print("picked up")
            time.sleep(10)
        else:
            print("can't pick up order")
            print(response.json())
            continue_flag = False


# ----------------------------------------------
def set_location(driver_token):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_token
    }
    dateInBaghdad = str(datetime.now(pytz.timezone('Asia/Baghdad')).date())
    timeInBaghdad = str(datetime.now(pytz.timezone('Asia/Baghdad')).time())[0:5]
    payload = {
        "latitude": latitude,
        "longitude": longitude,
        "distance": "50",
        "speed": "60",
        "accuracy": "10",
        "timestamp": dateInBaghdad + "T" + timeInBaghdad + ":00"
    }
    url = ApiData.location_api_url + "/location/"
    requests.request("POST", url, data=payload, headers=headers)


# script start:
# -------------------------------------------------------
continue_flag = False
admin_access_token = ""
driver_username = ""
driver_access_token = ""
driver_id = ""
order_ids = []

# -------------------------------------------------------

# login with super admin

login_response = AuthEndPoints.api_login(admin_username, admin_password)
if login_response.status_code == 200:
    admin_access_token = login_response.json()['data']['access_token']
    print("admin logged in successfully")
    continue_flag = True

# -------------------------------------------------------
# get drivers
if continue_flag:
    response = get_drivers(store_id, admin_access_token, driver_status)
    if response.status_code == 200 and response.json()['data']['num_records'] > 0:
        driver_username = response.json()['data']['page_records'][which_driver]['driver_info']['username']
        print("drivers with selected status have been found: " + str(driver_username) + str(driver_id))

    else:
        print("can't get drivers with the selected status")
        print(response.json())
        continue_flag = False

# -----------------------------------------------------

# login with driver and get his access token and id
if continue_flag:
    response = AuthEndPoints.api_login(driver_username, "P@ssw0rd")
    if response.status_code == 200:
        driver_access_token = response.json()['data']['access_token']
        driver_id = response.json()['data']['user']['driver_id']
        print("driver with id: " + str(driver_id) + " has been logged in successfully")
    else:
        print("driver can't login")
        print(response.status_code)
        continue_flag = False

# -----------------------------------------------------


# get assigned order of that driver
if continue_flag:
    response = get_orders(admin_access_token, driver_id, order_Status)
    if response.status_code == 200 and response.json()['data']['num_records'] > 0:
        for i in response.json()['data']['page_records']:
            x = i['id']
            order_ids.append(x)
        print("orders with selected stauts has been found: " + str(order_ids))
    else:
        print("can't get orders with the selected status")
        print(response.json())
        continue_flag = False

# -------------------------------------------
# change status to Picked Up
if continue_flag and int(order_Status) == 3:
    pickup(order_status=4, admin_token=admin_access_token, orders=order_ids)

# -------------------------------------------------------------

# change driver status to outward
if continue_flag and int(driver_status) == 2:
    payload = json.dumps({
        "driver_status_id": 6,
        "order_id": order_ids[0]
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_access_token
    }
    time.sleep(15)
    url = environment_url + "/drivers/update_driver_status/" + str(driver_id)

    print("waiting for system to allow moving outward...")
    status: int
    for x in range(20):
        status = requests.request("PUT", url, headers=headers, data=payload).status_code
        if status == 200:
            break
        time.sleep(6)

    if status == 200:
        print("outward")
        time.sleep(5)
        driver_status = 6
    else:
        print("response of changing driver status to outward: " + str(response.json()))
        print(status)
        continue_flag = False

# ------------------------------------------------

# change status to at address
if continue_flag and int(driver_status) == 6:
    payload = json.dumps({
        "driver_status_id": 7,
        "order_id": order_ids[0]
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_access_token
    }

    url = environment_url + "/drivers/update_driver_status/" + str(driver_id)
    response = requests.request("PUT", url, headers=headers, data=payload)

    if response.status_code == 200:
        print("at address")
        time.sleep(5)
        driver_status = 7
    else:
        print("response of changing driver status to at address: " + str(response.json()))
# -----------------------------------------------------

# deliver order
if continue_flag and int(driver_status) == 7:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + driver_access_token
    }

    url = environment_url + "/order/order_delivered/" + str(order_ids[0])
    response = requests.request("PUT", url, headers=headers)

    if response.status_code == 200:
        print("order delivered")
    else:
        print("response of deliver order: " + str(response.json()))

# ---------------------------------------------------
# set driver location at store
set_location(driver_access_token)

# set driver idle
payload = json.dumps({
        "driver_status_id": 3,
        "order_id": 0
    })

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + driver_access_token
}

url = environment_url + "/drivers/update_driver_status/" + str(driver_id)
response = requests.request("PUT", url, headers=headers, data=payload)

assert status == 200, print(status)
print("driver is at store")
