from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from API.driver_api import DriverEndPoints
from core.base_class_api import BaseApiClass


class APIRefreshToken(BaseApiClass):

    def setUp(self):
        super().setUp()
        login_response = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password)
        AuthEndPoints.login_token = login_response.json()['data'].get('access_token')
        AuthEndPoints.refresh_token = login_response.json()['data'].get('refresh_token')
        refresh_token_response = AuthEndPoints.api_refresh_token(self.BASE_URL, AuthEndPoints.refresh_token)
        AuthEndPoints.refresh_token_status_code = refresh_token_response.status_code
        AuthEndPoints.refresh_token_body = refresh_token_response.json()

    # Refresh token response with 200
    # TPI-T445  step 1
    def test_api_refresh_token_statuscode(self):
        self.assertTrue(AuthEndPoints.refresh_token_status_code == 200)

    # Assuming 'access_token' is a key in the response body
    # TPI-T445  step 2
    def test_api_refresh_token_access_token_token(self):
        self.assertIsNotNone(AuthEndPoints.refresh_token_body['data'].get('access_token'))

    # Assuming 'refresh_token' is a key in the response body
    # TPI-T445  step 3
    def test_api_refresh_token_refresh_token_token(self):
        self.assertIsNotNone(AuthEndPoints.refresh_token_body['data'].get('refresh_token'))

    # Verified 'last_name' is a string or null
    # TPI-T445  step 4
    def test_api_refresh_token_user_last_name(self):
        if self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['last_name']), str):
            return True
        elif type(AuthEndPoints.refresh_token_body['data']['user']['last_name']) is None:
            return True
        else:
            return False

    # Verified 'created_at' is a string
    # TPI-T445  step 5
    def test_api_refresh_token_user_created_at(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['created_at']), str)

    # Verified 'activated' is a string
    # TPI-T445  step 6
    def test_api_refresh_token_user_activated(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['activated']), bool)

    # Verified 'street' is a string
    # TPI-T445  step 7
    def test_api_refresh_token_user_street(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['street']), str)

    # Verified 'last_login' is a string
    # TPI-T445  step 8
    def test_api_refresh_token_user_last_login(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['last_login']), str)

    # Verified 'is_locked' is a string
    # TPI-T445  step 9
    def test_api_refresh_token_user_is_locked(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['is_locked']), bool)

    # Verified 'is_admin' is a string
    # TPI-T445  step 10
    def test_api_refresh_token_user_is_admin(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['is_admin']), bool)

    # Verified 'user_email' is a string
    # TPI-T445  step 11
    def test_api_refresh_token_user_user_email(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['user_email']), str)

    # Verified 'user_phone_number' is a string
    # TPI-T445  step 12
    def test_api_refresh_token_user_user_phone_number(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['user_phone_number']), str)

    # Verified 'birthdate' is a string
    # TPI-T445  step 13
    def test_api_refresh_token_user_birthdate(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['birthdate']), str)

    # Verified 'id' is a string
    # TPI-T445  step 14
    def test_api_refresh_token_user_id(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['id']), int)

    # Verified 'is_logged_out' is a string
    # TPI-T445  step 15
    def test_api_refresh_token_user_is_logged_out(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['is_logged_out']), bool)

    # Verified 'modified_at' is a string
    # TPI-T445  step 16
    def test_api_refresh_token_user_modified_at(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['modified_at']), str)

    # Verified 'first_name' is a string
    # TPI-T445  step 17
    def test_api_refresh_token_user_first_name(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['first_name']), str)

    # Verified 'username' is a string
    # TPI-T445  step 18
    def test_api_refresh_token_user_username(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['username']), str)

    # Verified 'role' is a dict
    # TPI-T445  step 19
    def test_api_refresh_token_user_role(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['role']), dict)

    # Verified 'role_value' is a str
    # TPI-T445  step 20
    def test_api_refresh_token_user_role_value(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['role']['value']), str)

    # Verified 'role_name' is a str
    # TPI-T445  step 21
    def test_api_refresh_token_user_role_name(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['role']['name']), str)

    # Verified 'role_id' is int
    # TPI-T445  step 22
    def test_api_refresh_token_user_role_id(self):
        self.assertEqual(type(AuthEndPoints.refresh_token_body['data']['user']['role']['id']), int)


class APIRefreshTokenPermission(BaseApiClass):

    def setUp(self):
        super().setUp()
        login_response = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password)
        AuthEndPoints.refresh_token = login_response.json()['data'].get('refresh_token')
        refresh_token_response = AuthEndPoints.api_refresh_token(self.BASE_URL, AuthEndPoints.refresh_token)
        AuthEndPoints.refresh_token_access_token = refresh_token_response.json()['data'].get('access_token')
        drivers_page_response = DriverEndPoints.api_drivers_page(self.BASE_URL, AuthEndPoints.refresh_token_access_token)
        DriverEndPoints.drivers_page_status_code = drivers_page_response.status_code
        DriverEndPoints.drivers_page_body = drivers_page_response.json()

    # Verified driver page response status code
    # TPI-T446  step 1
    def test_api_refresh_token_permission_status_code(self):
        self.assertTrue(DriverEndPoints.drivers_page_status_code == 200)

    # Verified driver page response body
    # TPI-T446  step 2
    def test_api_refresh_token_permission_body(self):
        self.assertEqual(type(DriverEndPoints.drivers_page_body['info']), dict)
        self.assertEqual(type(DriverEndPoints.drivers_page_body['data']), dict)
