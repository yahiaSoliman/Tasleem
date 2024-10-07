from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriverClockOutStatusDriverId(BaseApiClass):

    def setUp(self):
        super().setUp()
        global driver_id
        global driver_token
        global driver_clock_out_status_res
        driver_id = AuthEndPoints.api_login(self.BASE_URL, ApiData.driver_username, ApiData.driver_password).json()['data']['user'].get('driver_id')
        driver_token = AuthEndPoints.api_login(self.BASE_URL, ApiData.driver_username, ApiData.driver_password).json()['data'].get('access_token')
        driver_clock_out_status_res = DriverEndPoints.api_driver_driver_clock_out_status_driver_id(self.BASE_URL, driver_token, driver_id, params={})

    # Drivers driver clock out status driver id response with 200
    #   step 1
    def test_api_drivers_driver_clock_out_status_statuscode(self):
        self.assertTrue(driver_clock_out_status_res.status_code == 200)

    # Drivers driver clock out status driver id response data is dist
    #  step 2
    def test_api_drivers_driver_clock_out_status_data(self):
        self.assertTrue(type(driver_clock_out_status_res.json()['data']) == dict)

    # Drivers driver clock out status driver id response data_request_has_sent is bool
    #   step 3
    def test_api_drivers_driver_clock_out_status_data_request_has_sent(self):
        self.assertTrue(type(driver_clock_out_status_res.json()['data']['request_has_sent']) == bool)

    # Drivers driver clock out status driver id response data_request_has_approved is bool
    #   step 4
    def test_api_drivers_driver_clock_out_status_data_request_has_approved(self):
        self.assertTrue(type(driver_clock_out_status_res.json()['data']['request_has_approved']) == bool)
