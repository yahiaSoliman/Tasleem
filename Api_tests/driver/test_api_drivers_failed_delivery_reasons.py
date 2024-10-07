from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriveFailedDeliveryReasons(BaseApiClass):

    def setUp(self):
        super().setUp()
        global superadmintoken
        global drivers_driver_failed_delivery_reasons
        superadmintoken = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password).json()['data'].get('access_token')
        drivers_driver_failed_delivery_reasons = DriverEndPoints.api_driver_failed_delivery_reasons(self.BASE_URL, superadmintoken, params={})

    # Drivers driver failed delivery reasons response with 200
    #   step 1
    def test_api_drivers_driver_failed_delivery_reasons_status_code(self):
        self.assertTrue(drivers_driver_failed_delivery_reasons.status_code == 200)

    # Drivers driver failed delivery reasons response data is list
    #  step 2
    def test_api_drivers_driver_failed_delivery_reasons_data(self):
        self.assertTrue(type(drivers_driver_failed_delivery_reasons.json()['data']) == list)

    # Drivers driver failed delivery reasons response data_reason_value is str
    #   step 3
    def test_api_drivers_driver_failed_delivery_reasons_data_reason_value(self):
        self.assertTrue(type(drivers_driver_failed_delivery_reasons.json()['data'][0]['reason_value']) == str)

    # Drivers driver failed delivery reasons response data_reason_name is str
    #   step 4
    def test_api_drivers_driver_failed_delivery_reasons_data_reason_name(self):
        self.assertTrue(
            type(drivers_driver_failed_delivery_reasons.json()['data'][0]['reason_name']) == str)

    # Drivers driver failed delivery reasons response data_reason_id is int
    #  step 5
    def test_api_drivers_driver_failed_delivery_reasons_data_reason_id(self):
        self.assertTrue(type(drivers_driver_failed_delivery_reasons.json()['data'][0]['reason_id']) == int)
