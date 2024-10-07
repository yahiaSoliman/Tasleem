"""
this script helps in clock in multiple drivers
script user packages that get the baghdad time independently, so no need
for converting to any timezone
"""
import json
from datetime import date, datetime

import pytz
import requests

from API.auth_api import AuthEndPoints
from core.api_data import ApiData

store_latitude = input("please insert store latitude: ") or ApiData.store_lat
store_longitude = input("please insert store longitude: ") or ApiData.store_long

n = int(input("please enter number of drivers: "))
driver_usernames = []
for x in range(0, n):
    driver_usernames.append(input("enter username: "))

password = input("please enter the password of all users: ") or "P@ssw0rd"

for x in driver_usernames:
    login_response = AuthEndPoints.api_login(x, password)
    assert login_response.status_code == 200, print(login_response.json())
    access_token = login_response.json()['data']['access_token']
    driver_id = login_response.json()['data']['user']['driver_id']

    timeInBaghdad = str(datetime.now(pytz.timezone('Asia/Baghdad')).time())[0:5]

    payload = json.dumps({
        "status": "clock_in",
        "clock": timeInBaghdad + ":00",
        "clock_in_longitude": store_longitude,
        "clock_in_latitude": store_latitude
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }

    url = ApiData.api_url + f'/drivers/clock/{driver_id}'
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
