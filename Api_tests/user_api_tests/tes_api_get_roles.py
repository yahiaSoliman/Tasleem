from API.auth_api import AuthEndPoints
from API.user_api import UserApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiGetRoles(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global login_response
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # get roles
        global get_roles_response
        get_roles_response = UserApi.get_roles(access_token)

    def test_code_status(self):
        self.assertEqual(200, get_roles_response.status_code)

    def test_super_admin_role_id(self):
        self.assertEqual(1, get_roles_response.json()['data'][0]['id'])

    def test_super_admin_role_name(self):
        self.assertEqual("super_admin", get_roles_response.json()['data'][0]['name'])

    def test_super_admin_role_value(self):
        self.assertEqual("SuperAdmin", get_roles_response.json()['data'][0]['value'])

    def test_admin_role_id(self):
        self.assertEqual(2, get_roles_response.json()['data'][1]['id'])

    def test_admin_role_name(self):
        self.assertEqual("admin", get_roles_response.json()['data'][1]['name'])

    def test_admin_role_value(self):
        self.assertEqual("Admin", get_roles_response.json()['data'][1]['value'])

    def test_driver_role_id(self):
        self.assertEqual(3, get_roles_response.json()['data'][2]['id'])

    def test_driver_role_name(self):
        self.assertEqual("driver", get_roles_response.json()['data'][2]['name'])

    def test_driver_role_value(self):
        self.assertEqual("Driver", get_roles_response.json()['data'][2]['value'])

    def test_viewer_role_id(self):
        self.assertEqual(4, get_roles_response.json()['data'][3]['id'])

    def test_viewer_role_name(self):
        self.assertEqual("viewer", get_roles_response.json()['data'][3]['name'])

    def test_viewer_role_value(self):
        self.assertEqual("Viewer", get_roles_response.json()['data'][3]['value'])
