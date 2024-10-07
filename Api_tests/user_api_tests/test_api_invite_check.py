import random
import string

from API.auth_api import AuthEndPoints
from API.user_api import UserApi
from API.vehicles_api import VehicleAPI
from API.work_shift_api import WorkShiftApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiInviteCheck(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global access_token
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

    def test_super_admin_invitation_check(self):
        email = ''.join(random.choices(string.ascii_lowercase, k=7)) + "@gmail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 1
        })
        invitation_code = str(invite_user_response.json()['data']['invite_link'][-5:])
        user_name = ''.join(random.choices(string.ascii_lowercase, k=5))
        phone_number = ''.join(random.choices(string.digits, k=11))
        invite_check_response = UserApi.invite_check_user(parameters={'user_email': email, 'code': invitation_code},
                                                          body={
                                                              "first_name": "UO",
                                                              "last_name": "UI",
                                                              "username": user_name,
                                                              "birthdate": "2023-01-05T01:33:00",
                                                              "user_phone_number": phone_number,
                                                              "password": "testTest1!",
                                                              "street": "33333",
                                                              "driver_license_no": "",
                                                              "city_id": 2,
                                                              "user_email": email,
                                                              "box_number": "",
                                                              "address_building": "",
                                                              "address_district": "",
                                                              "address_flat": "",
                                                              "address_floor": "",
                                                              "address_nearest_landmark": "",
                                                              "address_neighborhood": ""
                                                          })
        self.assertEqual(200, invite_check_response.status_code)
        self.assertEqual("Registration completed", invite_check_response.json()['info']['message'])

    def test_admin_invitation_check(self):
        email = ''.join(random.choices(string.ascii_lowercase, k=7)) + "@gmail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 2
        })
        invitation_code = str(invite_user_response.json()['data']['invite_link'][-5:])
        user_name = ''.join(random.choices(string.ascii_lowercase, k=5))
        phone_number = ''.join(random.choices(string.digits, k=11))
        invite_check_response = UserApi.invite_check_user(parameters={'user_email': email, 'code': invitation_code},
                                                          body={
                                                                  "first_name": "first_name",
                                                                  "last_name": "last_name",
                                                                  "username": user_name,
                                                                  "birthdate": "2024-01-01T01:05:00",
                                                                  "user_phone_number": phone_number,
                                                                  "password": "P@ssw0rd",
                                                                  "street": "dd",
                                                                  "driver_license_no": "",
                                                                  "city_id": 1,
                                                                  "user_email": email,
                                                                  "box_number": "",
                                                                  "address_building": "",
                                                                  "address_district": "",
                                                                  "address_flat": "",
                                                                  "address_floor": "",
                                                                  "address_nearest_landmark": "",
                                                                  "address_neighborhood": ""
                                                          })
        self.assertEqual(200, invite_check_response.status_code)
        self.assertEqual("Registration completed", invite_check_response.json()['info']['message'])

    def test_driver_invitation_check(self):
        # create vehicle to be assigned to the driver
        license_number = ''.join(random.choices(string.ascii_lowercase +
                                                string.digits, k=7))
        create_vehicle_response = VehicleAPI.create_vehicle(access_token,
                                                            payload_dict={
                                                                "name": "testName",
                                                                "model": "2101",
                                                                "make": "testMake",
                                                                "year": 1960,
                                                                "license_no": license_number,
                                                                "vehicle_type_id": 1,
                                                                "owner": "driver"
                                                            })
        vehicle_id = create_vehicle_response.json()['info']['message']['id']

        # create work shift for the new driver
        shift_name = "automation_test_" + ''.join(random.choices(string.ascii_lowercase +
                                                                 string.digits, k=7))

        WorkShiftApi.create_work_shift(access_token, {
            "name": shift_name,
            "value": "test_value",
            "darkstore_id": 1,
            "shift_start": "15:00:00",
            "shift_end": "23:00:00",
            "description": "test_description"
        })

        # get work shift id
        response = WorkShiftApi.get_all_work_shifts(access_token, {"search": shift_name})
        work_shift_id = response.json()['data']['page_records'][0]['id']

        # crate invitation for the new driver
        email = ''.join(random.choices(string.ascii_lowercase, k=7)) + "@gmail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 3,
            "dark_store_id": 1,
            "vehicle_id": vehicle_id,
            "shift_id": work_shift_id
        })
        invitation_code = str(invite_user_response.json()['data']['invite_link'][-5:])
        user_name = ''.join(random.choices(string.ascii_lowercase, k=5))
        phone_number = ''.join(random.choices(string.digits, k=11))

        # check invitation of the new driver
        invite_check_response = UserApi.invite_check_user(parameters={'user_email': email, 'code': invitation_code},
                                                          body={
                                                                  "first_name": "first_name",
                                                                  "last_name": "last_name",
                                                                  "username": user_name,
                                                                  "birthdate": "2024-01-01T01:21:00",
                                                                  "user_phone_number": phone_number,
                                                                  "password": "P@ssw0rd",
                                                                  "street": "ddsd",
                                                                  "driver_license_no": "sd5656df",
                                                                  "city_id": 1,
                                                                  "user_email": email,
                                                                  "box_number": "d6f56",
                                                                  "address_building": "sdfsdfdsf",
                                                                  "address_district": "sdf",
                                                                  "address_flat": "sdf",
                                                                  "address_floor": "dsf",
                                                                  "address_nearest_landmark": "dsfds",
                                                                  "address_neighborhood": "dfsdf"
                                                          })
        self.assertEqual(200, invite_check_response.status_code)
        self.assertEqual("Registration completed", invite_check_response.json()['info']['message'])

    def test_viewer_invitation_check(self):
        email = ''.join(random.choices(string.ascii_lowercase, k=7)) + "@gmail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 4
        })
        invitation_code = str(invite_user_response.json()['data']['invite_link'][-5:])
        user_name = ''.join(random.choices(string.ascii_lowercase, k=5))
        phone_number = ''.join(random.choices(string.digits, k=11))
        invite_check_response = UserApi.invite_check_user(parameters={'user_email': email, 'code': invitation_code},
                                                          body={
                                                              "first_name": "first_name",
                                                              "last_name": "last_name",
                                                              "username": user_name,
                                                              "birthdate": "2024-01-01T01:05:00",
                                                              "user_phone_number": phone_number,
                                                              "password": "P@ssw0rd",
                                                              "street": "dd",
                                                              "driver_license_no": "",
                                                              "city_id": 1,
                                                              "user_email": email,
                                                              "box_number": "",
                                                              "address_building": "",
                                                              "address_district": "",
                                                              "address_flat": "",
                                                              "address_floor": "",
                                                              "address_nearest_landmark": "",
                                                              "address_neighborhood": ""
                                                          })
        self.assertEqual(200, invite_check_response.status_code)
        self.assertEqual("Registration completed", invite_check_response.json()['info']['message'])

