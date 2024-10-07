from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriverClockOutLocDriverId(BaseApiClass):

    def setUp(self):
        super().setUp()
        global driver_id
        global superadmintoken
        global driver_clock_out_loc_res
        global shift_id
        driver_id = AuthEndPoints.api_login(self.BASE_URL, ApiData.driver_username, ApiData.driver_password).json()['data']['user'].get('driver_id')
        superadmintoken = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password).json()['data'].get('access_token')
        shift_id = DriverEndPoints.api_driver_driver_id(self.BASE_URL, superadmintoken, driver_id, params={}).json()['data']['shift'].get('id')
        driver_clock_out_loc_res = DriverEndPoints.api_driver_driver_clock_out_loc_driver_id(self.BASE_URL, superadmintoken, driver_id, params={'shift_id': shift_id})

    # Drivers driver clock out loc driver id response with 200
    #   step 1
    def test_api_drivers_driver_clock_out_loc_statuscode(self):
        self.assertTrue(driver_clock_out_loc_res.status_code == 200)

    # Drivers driver clock out loc driver id response data is dist
    #  step 2
    def test_api_drivers_driver_clock_out_loc_data(self):
        self.assertTrue(type(driver_clock_out_loc_res.json()['data']) == dict)

    # Drivers driver clock out loc driver id response data_current_driver_latitude is str
    #   step 3
    def test_api_drivers_driver_clock_out_loc_data_current_driver_latitude(self):
        self.assertTrue(type(driver_clock_out_loc_res.json()['data']['current_driver_latitude']) == str)

    # Drivers driver clock out loc driver id response data_current_driver_longitude is str
    #   step 4
    def test_api_drivers_driver_clock_out_loc_data_current_driver_longitude(self):
        self.assertTrue(type(driver_clock_out_loc_res.json()['data']['current_driver_longitude']) == str)
