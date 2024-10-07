from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from API.driver_api import DriverEndPoints
from core.base_class_api import BaseApiClass


class APILogoutResponse(BaseApiClass):

    def setUp(self):
        super().setUp()
        login_response = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password)
        AuthEndPoints.login_token = login_response.json()['data'].get('access_token')
        logout_response = AuthEndPoints.api_logout(self.BASE_URL, AuthEndPoints.login_token)
        AuthEndPoints.logout_status_code = logout_response.status_code
        AuthEndPoints.logout_body = logout_response.json()

    # Verified log out status code
    # TPI-T443  step 1
    def test_api_logout_status_code(self):
        self.assertTrue(AuthEndPoints.logout_status_code == 200)

    # Verified log out response massage
    # TPI-T443  step 2
    def test_api_logout_massage(self):
        self.assertTrue(AuthEndPoints.logout_body['info']['message'] == "You log out successfully")


class APILogoutPermission(BaseApiClass):

    def setUp(self):
        super().setUp()
        login_response = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password)
        AuthEndPoints.login_token = login_response.json()['data'].get('access_token')
        AuthEndPoints.api_logout(self.BASE_URL, AuthEndPoints.login_token)
        drivers_page_response = DriverEndPoints.api_drivers_page(self.BASE_URL, AuthEndPoints.login_token)
        DriverEndPoints.drivers_page_status_code = drivers_page_response.status_code
        DriverEndPoints.drivers_page_body = drivers_page_response.json()

    # Verified unable to request status code
    # TPI-T444  step 1
    def test_api_logout_status_code(self):
        self.assertTrue(DriverEndPoints.drivers_page_status_code == 401)

    # Verified unable to request response massage
    # TPI-T444  step 2
    def test_api_logout_massage(self):
        self.assertTrue(DriverEndPoints.drivers_page_body['info']['message'] == "authorization required.")