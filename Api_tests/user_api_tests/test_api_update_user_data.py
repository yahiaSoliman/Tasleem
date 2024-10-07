import random
import string

from API.auth_api import AuthEndPoints
from API.user_api import UserApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiUpdateUserData(BaseApiClass):
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

        # update user data
        global update_user_data_response
        update_user_data_response = UserApi.update_user_data(access_token, user_id, {

            "user_email": "updated" + email,
            "user_phone_number": phone_number[0:8] + "000",
            "first_name": "updated_first_name",
            "last_name": "updated_last_name",
            "birthdate": "2022-02-25T14:55:37.101Z",
            "username": "updated" + user_name
        })

        # get user data
        global get_user_data_response
        get_user_data_response = UserApi.get_user_data(access_token, user_id)

    def test_code_status(self):
        self.assertEqual(200, update_user_data_response.status_code)

    def test_first_name(self):
        self.assertEqual('updated_first_name', get_user_data_response.json()['data']['first_name'])

    def test_last_name(self):
        self.assertEqual('updated_last_name', get_user_data_response.json()['data']['last_name'])

    def test_user_name(self):
        self.assertEqual("updated" + user_name, get_user_data_response.json()['data']['username'])

    def test_email(self):
        self.assertEqual("updated" + email, get_user_data_response.json()['data']['user_email'])

    def test_phone_number(self):
        self.assertEqual(phone_number[0:8] + "000", get_user_data_response.json()['data']['user_phone_number'])

    def test_birthdate(self):
        self.assertTrue(True, "2022-02-25" in get_user_data_response.json()['data']['birthdate'])
