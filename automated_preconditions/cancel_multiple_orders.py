"""

the following script allows the tester to cancel all orders of certain
darkstore and status id as many as there are in the store. it can be helpful
for getting the status of the store clean and clear for assigning new orders

"""

import json
import requests
from core.api_data import ApiData

"""
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
environment_url = ApiData.api_url
admin_username = ApiData.superadmin_username
admin_password = ApiData.superadmin_password
store_id = input("please insert store id: ") or 5
order_Status_id = input("please insert order status id: ") or 3


# login
payload_login = json.dumps({
    "username": admin_username,
    "password": admin_password
})

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
url_login = environment_url + "/auth/login"
response = requests.request("POST", url_login, headers=headers, data=payload_login)
access_token = response.json()['data']['access_token']

# ------------------------------------------------------------------
# ------------------------------------------------------------------

# get orders
parameters = {
    'page_number': 1,
    'per_page': 3000,
    'dark_store_ids': store_id,
    'order_status_ids': order_Status_id
}
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + access_token
}

url = environment_url + '/order/page'
response_of_get_all_orders = requests.request("GET", url, headers=headers, params=parameters)

# ------------------------------------------------------------------
# ------------------------------------------------------------------

# cancel orders
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + access_token
}
payload = json.dumps({

    "order_status_id": 12
})

if response_of_get_all_orders.json()['data']['num_records'] > 0:
    for order_details in response_of_get_all_orders.json()['data']['page_records']:
        url = environment_url + "/order/update_order_status_internally/" + str(order_details['id'])
        response = requests.request("PUT", url, headers=headers, data=payload)
        print(response.json())
else:
    print("no orders with selected status")

