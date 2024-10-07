from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass


class APILoginTestSuperAdmin(BaseApiClass):


    def setUp(self):
        super().setUp()
        response = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password)
        AuthEndPoints.login_status_code = response.status_code
        AuthEndPoints.login_body = response.json()

    # Login response with 200
    # TPI-T440  step 1
    def test_api_login_statuscode(self):
        self.assertTrue(AuthEndPoints.login_status_code == 200)

    # Assuming 'access_token' is a key in the response body
    # TPI-T440  step 2
    def test_api_login_access_token_token(self):
        self.assertIsNotNone(AuthEndPoints.login_body['data'].get('access_token'))

    # Assuming 'refresh_token' is a key in the response body
    # TPI-T440  step 3
    def test_api_login_refresh_token_token(self):
        self.assertIsNotNone(AuthEndPoints.login_body['data'].get('refresh_token'))

    # Verified 'last_name' is a string or null
    # TPI-T440  step 4
    def test_api_login_user_last_name(self):
        if self.assertEqual(type(AuthEndPoints.login_body['data']['user']['last_name']), str):
            return True
        elif type(AuthEndPoints.login_body['data']['user']['last_name']) is None:
            return True
        else:
            return False

    # Verified 'created_at' is a string
    # TPI-T440  step 5
    def test_api_login_user_created_at(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['created_at']), str)

    # Verified 'activated' is a string
    # TPI-T440  step 6
    def test_api_login_user_activated(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['activated']), bool)

    # Verified 'street' is a string
    # TPI-T440  step 7
    def test_api_login_user_street(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['street']), str)

    # Verified 'last_login' is a string
    # TPI-T440  step 8
    def test_api_login_user_last_login(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['last_login']), str)

    # Verified 'is_locked' is a string
    # TPI-T440  step 9
    def test_api_login_user_is_locked(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_locked']), bool)

    # Verified 'is_admin' is a string
    # TPI-T440  step 10
    def test_api_login_user_is_admin(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_admin']), bool)

    # Verified 'user_email' is a string
    # TPI-T440  step 11
    def test_api_login_user_user_email(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['user_email']), str)

    # Verified 'user_phone_number' is a string
    # TPI-T440  step 12
    def test_api_login_user_user_phone_number(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['user_phone_number']), str)

    # Verified 'birthdate' is a string
    # TPI-T440  step 13
    def test_api_login_user_birthdate(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['birthdate']), str)

    # Verified 'id' is a string
    # TPI-T440  step 14
    def test_api_login_user_id(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['id']), int)

    # Verified 'is_logged_out' is a string
    # TPI-T440  step 15
    def test_api_login_user_is_logged_out(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_logged_out']), bool)

    # Verified 'modified_at' is a string
    # TPI-T440  step 16
    def test_api_login_user_modified_at(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['modified_at']), str)

    # Verified 'first_name' is a string
    # TPI-T440  step 17
    def test_api_login_user_first_name(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['first_name']), str)

    # Verified 'username' is a string
    # TPI-T440  step 18
    def test_api_login_user_username(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['username']), str)

    # Verified 'role' is a dict
    # TPI-T440  step 19
    def test_api_login_user_role(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']), dict)

    # Verified 'role_value' is a str
    # TPI-T440  step 20
    def test_api_login_user_role_value(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['value']), str)

    # Verified 'role_name' is a str
    # TPI-T440  step 21
    def test_api_login_user_role_name(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['name']), str)

    # Verified 'role_id' is int
    # TPI-T440  step 22
    def test_api_login_user_role_id(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['id']), int)


class APILoginTestDriver(BaseApiClass):

    def setUp(self):
        super().setUp()
        response = AuthEndPoints.api_login(self.BASE_URL, ApiData.driver_username, ApiData.driver_password)
        AuthEndPoints.login_status_code = response.status_code
        AuthEndPoints.login_body = response.json()

    # Login response with 200
    # TPI-T441  step 1
    def test_api_login_statuscode(self):
        self.assertTrue(AuthEndPoints.login_status_code == 200)

    # Assuming 'access_token' is a key in the response body
    # TPI-T441  step 2
    def test_api_login_access_token_token(self):
        self.assertIsNotNone(AuthEndPoints.login_body['data'].get('access_token'))

    # Assuming 'refresh_token' is a key in the response body
    # TPI-T441  step 3
    def test_api_login_refresh_token_token(self):
        self.assertIsNotNone(AuthEndPoints.login_body['data'].get('refresh_token'))

    # Verified 'last_name' is a string or null
    # TPI-T441  step 4
    def test_api_login_user_last_name(self):
        if self.assertEqual(type(AuthEndPoints.login_body['data']['user']['last_name']), str):
            return True
        elif type(AuthEndPoints.login_body['data']['user']['last_name']) is None:
            return True
        else:
            return False

    # Verified 'created_at' is a string
    # TPI-T441  step 5
    def test_api_login_user_created_at(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['created_at']), str)

    # Verified 'activated' is a string
    # TPI-T441  step 6
    def test_api_login_user_activated(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['activated']), bool)

    # Verified 'street' is a string
    # TPI-T441  step 7
    def test_api_login_user_street(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['street']), str)

    # Verified 'last_login' is a string
    # TPI-T441  step 8
    def test_api_login_user_last_login(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['last_login']), str)

    # Verified 'is_locked' is a string
    # TPI-T441  step 9
    def test_api_login_user_is_locked(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_locked']), bool)

    # Verified 'is_admin' is a string
    # TPI-T441  step 10
    def test_api_login_user_is_admin(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_admin']), bool)

    # Verified 'user_email' is a string
    # TPI-T441  step 11
    def test_api_login_user_user_email(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['user_email']), str)

    # Verified 'user_phone_number' is a string
    # TPI-T441  step 12
    def test_api_login_user_user_phone_number(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['user_phone_number']), str)

    # Verified 'birthdate' is a string
    # TPI-T441  step 13
    def test_api_login_user_birthdate(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['birthdate']), str)

    # Verified 'id' is a string
    # TPI-T441  step 14
    def test_api_login_user_id(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['id']), int)

    # Verified 'is_logged_out' is a string
    # TPI-T441  step 15
    def test_api_login_user_is_logged_out(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_logged_out']), bool)

    # Verified 'modified_at' is a string
    # TPI-T441  step 16
    def test_api_login_user_modified_at(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['modified_at']), str)

    # Verified 'first_name' is a string
    # TPI-T441  step 17
    def test_api_login_user_first_name(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['first_name']), str)

    # Verified 'username' is a string
    # TPI-T441  step 18
    def test_api_login_user_username(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['username']), str)

    # Verified 'role' is a dict
    # TPI-T441  step 19
    def test_api_login_user_role(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']), dict)

    # Verified 'role_value' is a str
    # TPI-T441  step 20
    def test_api_login_user_role_value(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['value']), str)

    # Verified 'role_name' is a str
    # TPI-T441  step 21
    def test_api_login_user_role_name(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['name']), str)

    # Verified 'role_id' is int
    # TPI-T441  step 22
    def test_api_login_user_role_id(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['id']), int)

    # Verified 'driver_id' is int
    # TPI-T441  step 23
    def test_api_login_user_driver_id(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['driver_id']), int)


class APILoginTestAdmin(BaseApiClass):

    def setUp(self):
        super().setUp()
        response = AuthEndPoints.api_login(self.BASE_URL, ApiData.driver_username, ApiData.driver_password)
        AuthEndPoints.login_status_code = response.status_code
        AuthEndPoints.login_body = response.json()

    # Login response with 200
    # TPI-T442  step 1
    def test_api_login_statuscode(self):
        self.assertTrue(AuthEndPoints.login_status_code == 200)

    # Assuming 'access_token' is a key in the response body
    # TPI-T442  step 2
    def test_api_login_access_token_token(self):
        self.assertIsNotNone(AuthEndPoints.login_body['data'].get('access_token'))

    # Assuming 'refresh_token' is a key in the response body
    # TPI-T442  step 3
    def test_api_login_refresh_token_token(self):
        self.assertIsNotNone(AuthEndPoints.login_body['data'].get('refresh_token'))

    # Verified 'last_name' is a string or null
    # TPI-T442  step 4
    def test_api_login_user_last_name(self):
        if self.assertEqual(type(AuthEndPoints.login_body['data']['user']['last_name']), str):
            return True
        elif type(AuthEndPoints.login_body['data']['user']['last_name']) is None:
            return True
        else:
            return False

    # Verified 'created_at' is a string
    # TPI-T442  step 5
    def test_api_login_user_created_at(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['created_at']), str)

    # Verified 'activated' is a string
    # TPI-T442  step 6
    def test_api_login_user_activated(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['activated']), bool)

    # Verified 'street' is a string
    # TPI-T442  step 7
    def test_api_login_user_street(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['street']), str)

    # Verified 'last_login' is a string
    # TPI-T442  step 8
    def test_api_login_user_last_login(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['last_login']), str)

    # Verified 'is_locked' is a string
    # TPI-T442  step 9
    def test_api_login_user_is_locked(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_locked']), bool)

    # Verified 'is_admin' is a string
    # TPI-T442  step 10
    def test_api_login_user_is_admin(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_admin']), bool)

    # Verified 'user_email' is a string
    # TPI-T442  step 11
    def test_api_login_user_user_email(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['user_email']), str)

    # Verified 'user_phone_number' is a string
    # TPI-T442  step 12
    def test_api_login_user_user_phone_number(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['user_phone_number']), str)

    # Verified 'birthdate' is a string
    # TPI-T442  step 13
    def test_api_login_user_birthdate(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['birthdate']), str)

    # Verified 'id' is a string
    # TPI-T442  step 14
    def test_api_login_user_id(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['id']), int)

    # Verified 'is_logged_out' is a string
    # TPI-T442  step 15
    def test_api_login_user_is_logged_out(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['is_logged_out']), bool)

    # Verified 'modified_at' is a string
    # TPI-T442  step 16
    def test_api_login_user_modified_at(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['modified_at']), str)

    # Verified 'first_name' is a string
    # TPI-T442  step 17
    def test_api_login_user_first_name(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['first_name']), str)

    # Verified 'username' is a string
    # TPI-T442  step 18
    def test_api_login_user_username(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['username']), str)

    # Verified 'role' is a dict
    # TPI-T442  step 19
    def test_api_login_user_role(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']), dict)

    # Verified 'role_value' is a str
    # TPI-T442  step 20
    def test_api_login_user_role_value(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['value']), str)

    # Verified 'role_name' is a str
    # TPI-T442  step 21
    def test_api_login_user_role_name(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['name']), str)

    # Verified 'role_id' is int
    # TPI-T442  step 22
    def test_api_login_user_role_id(self):
        self.assertEqual(type(AuthEndPoints.login_body['data']['user']['role']['id']), int)