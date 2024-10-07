import random
import string

from API.auth_api import AuthEndPoints
from API.user_api import UserApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiDeactivateUser(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        # login
        global access_token
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # create user
        global email
        email = ''.join(random.choices(string.ascii_lowercase, k=7)) + "@gmail.com"
        invite_user_response = UserApi.invite_user(access_token, bodyData={
            "user_email": email,
            "role_id": 2
        })
        invitation_code = str(invite_user_response.json()['data']['invite_link'][-5:])
        global user_name
        user_name = ''.join(random.choices(string.ascii_lowercase, k=5))
        global phone_number
        phone_number = ''.join(random.choices(string.digits, k=11))
        invite_check_response = UserApi.invite_check_user(parameters={'user_email': email, 'code': invitation_code},
                                                          body={
                                                              "first_name": "coco",
                                                              "last_name": "lovers",
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

        # get user id
        all_users_response = UserApi.get_all_users(access_token, {'search': user_name})
        user_id = all_users_response.json()['data']['page_records'][0]['id']

        # get user data
        global default_user_data
        default_user_data = UserApi.get_user_data(access_token, user_id)

        # deactivate user
        global deactivate_user_response
        deactivate_user_response = UserApi.deactivate_user(access_token, user_id)

        global user_data_after_deactivation
        user_data_after_deactivation = UserApi.get_user_data(access_token, user_id)

        # activate user
        global activate_user_response
        activate_user_response = UserApi.activate_user(access_token, user_id)

        global user_data_after_activation
        user_data_after_activation = UserApi.get_user_data(access_token, user_id)

    def test_code_status(self):
        self.assertEqual(200, deactivate_user_response.status_code)

    def test_success_message(self):
        self.assertEqual("user deactivated successfully.", deactivate_user_response.json()['info']['message'])

    def test_old_activation_status(self):
        self.assertEqual(True, default_user_data.json()['data']['activated'])

    def test_deactivation_status(self):
        self.assertEqual(False, user_data_after_deactivation.json()['data']['activated'])

    def test_activation_status(self):
        self.assertEqual(True, user_data_after_activation.json()['data']['activated'])
