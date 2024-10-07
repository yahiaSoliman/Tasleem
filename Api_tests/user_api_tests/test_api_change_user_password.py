import random
import string

from API.auth_api import AuthEndPoints
from API.user_api import UserApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiChangePassword(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global login_response
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # create user
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

        # get user id
        all_users_response = UserApi.get_all_users(access_token, {'search': user_name})
        user_id = all_users_response.json()['data']['page_records'][0]['id']

        # change password
        global change_password_response
        change_password_response = UserApi.change_user_password(access_token, user_id, {
            "new_password": "P#ssw0rd",
            "confirm_new_password": "P#ssw0rd"
        })

    def test_code_status(self):
        self.assertEqual(200, change_password_response.status_code)

    def test_success_message(self):
        self.assertEqual("Password updated successfully, please login again.", change_password_response.json()['info']['message'])
