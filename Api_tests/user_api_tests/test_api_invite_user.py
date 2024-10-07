import random
import string

from API.auth_api import AuthEndPoints
from API.user_api import UserApi
from API.vehicles_api import VehicleAPI
from API.work_shift_api import WorkShiftApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiInviteUser(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global access_token
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

    def test_super_admin_invitation(self):
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@mail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 1
        })
        self.assertEqual(200, invite_user_response.status_code)
        self.assertTrue(str(invite_user_response.json()['data']['invite_link']).__contains__("super_admin"))

    def test_admin_invitation(self):
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@mail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 2
        })
        self.assertEqual(200, invite_user_response.status_code)
        self.assertTrue(str(invite_user_response.json()['data']['invite_link']).__contains__("admin"))

    def test_driver_invitation(self):
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

        # invite driver
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@mail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 3,
            "dark_store_id": 1,
            "vehicle_id": vehicle_id,
            "shift_id": work_shift_id
        })
        self.assertEqual(200, invite_user_response.status_code)
        self.assertTrue(str(invite_user_response.json()['data']['invite_link']).__contains__("driver"))

    def test_viewer_invitation(self):
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@mail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 4
        })
        self.assertEqual(200, invite_user_response.status_code)
        self.assertTrue(str(invite_user_response.json()['data']['invite_link']).__contains__("viewer"))
