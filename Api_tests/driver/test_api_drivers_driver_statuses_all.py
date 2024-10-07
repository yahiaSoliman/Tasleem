from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriverStatusesAll(BaseApiClass):

    def setUp(self):
        super().setUp()
        global superadmintoken
        global drivers_driver_statuses_all
        superadmintoken = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password).json()['data'].get('access_token')
        drivers_driver_statuses_all = DriverEndPoints.api_driver_statuses_all(self.BASE_URL, superadmintoken, params={})

    # Drivers driver statuses all response with 200
    #   step 1
    def test_api_drivers_driver_statuses_all_status_code(self):
        self.assertTrue(drivers_driver_statuses_all.status_code == 200)

    # Drivers driver statuses all response data is list
    #  step 2
    def test_api_drivers_driver_statuses_all_data(self):
        self.assertTrue(type(drivers_driver_statuses_all.json()['data']) == list)

    # Drivers driver statuses all response data_value is str
    #   step 3
    def test_api_drivers_driver_statuses_all_data_value(self):
        self.assertTrue(type(drivers_driver_statuses_all.json()['data'][0]['value']) == str)

    # Drivers driver statuses all response data_name is str
    #   step 4
    def test_api_drivers_driver_statuses_all_data_name(self):
        self.assertTrue(
            type(drivers_driver_statuses_all.json()['data'][0]['name']) == str)

    # Drivers driver statuses all response data_id is int
    #  step 5
    def test_api_drivers_driver_statuses_all_data_id(self):
        self.assertTrue(type(drivers_driver_statuses_all.json()['data'][0]['id']) == int)

