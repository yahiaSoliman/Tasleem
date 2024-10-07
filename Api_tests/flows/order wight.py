"""
verify that zone with fewer orders are more prioritized if waiting time is longer
than orders of other zones
"""
import time

from API.auth_api import AuthEndPoints
from API.darkstore_api import DarkStoreApis
from API.order_api import OrderApis
from core.api_data import ApiData

"""
steps:
set interval time one minute
set weight equal to 4
get one idle driver
disable auto assignment
create one order in zone A
set order ready for pickup
wait for few minutes
create 3 orders in zone B
set orders ready for pickup
enable auto assignment
"""

"""
preconditions:
1 - two idle driver
2 - two zones are existed for darkstore
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

store_id_numeric = input("please insert store id: ") or 5
store_id_string = input("please insert store name: ") or ApiData.dark_store
zone_A_location_latitude = input("please insert latitude of first destination: ") or 33.417042
zone_A_location_longitude = input("please insert longitude of first destination: ") or 44.301094
zone_B_location_latitude = input("please insert latitude of second destination: ") or 33.4395571
zone_B_location_longitude = input("please insert longitude of second destination: ") or 44.2614315


def update_store_settings(token, store_id, stop_auto_assignment_flag):
    response = DarkStoreApis.api_update_store_settings(token, store_id, {
        "max_threshold_waiting_time": 20*60,
        "max_orders_assigned": 5,
        "email_address": "update-store@gmail.com",
        "max_distance_from_dark_store": 200,
        "score_divisor": 1,
        "interval_time": 60,
        "interval_weight": 4,
        "stop_auto_assignment": stop_auto_assignment_flag,
        "stop_auto_clock_out": True,
        "delivered_orders_count_weight": 0.5,
        "delivered_orders_distance_weight": 0.3,
        "waiting_time_at_the_darkstore_weight": 0.2
    })
    assert response.status_code == 200, print("can't update store settings")


def create_order(order_name, store_id, lat, long):
    response = OrderApis.api_create_auto_assignment_order(order_name, store_id, long, lat)
    assert response.status_code == 200, print(response.json())
    return response.json()['data']['id']


def get_order_details(token, order_id):
    response = OrderApis.api_get_order_by_id(order_id, token)
    return response.json()


def ready_for_pickup(order_id):
    response = OrderApis.set_ready_for_pickup_status(order_id)
    assert response.status_code == 200, print(response.json())


def verify_assignment(order_id):
    print("waiting for automatic assignment of order " + str(order_id) + " . . . ")
    for x in range(30):
        response = get_order_details(token=admin_access_token, order_id=order_id)
        if response['data']['order_status']['id'] == 3:
            break
        time.sleep(3)
    assert get_order_details(token=admin_access_token, order_id=order_id)['data']['order_status']['id'] == 3
    assigned_driver = get_order_details(token=admin_access_token, order_id=order_id)['data']['driver_id']
    assert get_order_details(token=admin_access_token, order_id=order_id)['data']['order_status_time'][2][
               'status'] == "assigned"
    timestamp = get_order_details(token=admin_access_token, order_id=order_id)['data']['order_status_time'][2]['value']
    print("order " + str(order_id) + " has been assigned to driver " + str(assigned_driver) + " at " + str(timestamp))


# flow starts:
# login with admin
print("------------------------------------------")
response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
assert response.status_code == 200, "can't login admin"
admin_access_token = response.json()['data']['access_token']
# disable auto assignment
update_store_settings(token=admin_access_token, store_id=store_id_numeric, stop_auto_assignment_flag=True)
print("store settings have been set successfully")

# create order
order_1 = create_order(order_name=order_id_string + "0", store_id=store_id_string, lat=zone_A_location_latitude,
                       long=zone_A_location_longitude)
zone_id = get_order_details(token=admin_access_token, order_id=order_1)['data']['zone_id']
print(str(order_1) + " has been created in zone " + str(zone_id))

ready_for_pickup(order_1)
print(str(order_1) + " is ready for pickup")

print("waiting for order to get higher weight . . . ")
time.sleep(180)

# create order
order_2 = create_order(order_name=order_id_string + "1", store_id=store_id_string, lat=zone_B_location_latitude,
                       long=zone_B_location_longitude)
zone_id = get_order_details(token=admin_access_token, order_id=order_2)['data']['zone_id']
print(str(order_2) + " has been created in zone " + str(zone_id))

# create order
order_3 = create_order(order_name=order_id_string + "2", store_id=store_id_string, lat=zone_B_location_latitude,
                       long=zone_B_location_longitude)
zone_id = get_order_details(token=admin_access_token, order_id=order_3)['data']['zone_id']
print(str(order_3) + " has been created in zone " + str(zone_id))

# create order
order_4 = create_order(order_name=order_id_string + "3", store_id=store_id_string, lat=zone_B_location_latitude,
                       long=zone_B_location_longitude)
zone_id = get_order_details(token=admin_access_token, order_id=order_4)['data']['zone_id']
print(str(order_4) + " has been created in zone " + str(zone_id))

ready_for_pickup(order_2)
print(str(order_2) + " is ready for pickup")

ready_for_pickup(order_3)
print(str(order_3) + " is ready for pickup")

ready_for_pickup(order_4)
print(str(order_4) + " is ready for pickup")


# enable auto assignment
update_store_settings(token=admin_access_token, store_id=store_id_numeric, stop_auto_assignment_flag=False)
print("auto assignment has been enabled")

# verify orders
verify_assignment(order_1)
verify_assignment(order_2)
verify_assignment(order_3)
verify_assignment(order_4)

