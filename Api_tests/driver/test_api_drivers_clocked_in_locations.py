from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriversClockInLocation(BaseApiClass):

    def setUp(self):
        super().setUp()
        global superadmintoken
        global drivers_clocked_in_locations_res
        superadmintoken = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password).json()['data'].get('access_token')
        drivers_clocked_in_locations_res = DriverEndPoints.api_drivers_clocked_in_locations(self.BASE_URL, superadmintoken, params={'search': 'aromanii'})

    # Drivers clock in location response with 200
    # TPI-T460  step 1
    def test_api_drivers_clocked_in_locations_statuscode(self):
        self.assertTrue(drivers_clocked_in_locations_res.status_code == 200)

    # Drivers clock in location response data is dist
    # TPI-T460  step 2
    def test_api_drivers_clocked_in_locations_data(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']) == dict)

    # Drivers clock in location response data_page_records is list
    # TPI-T460  step 3
    def test_api_drivers_clocked_in_locations_data_page_records(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records']) == list)

    # Drivers clock in location response data_page_records_driver_status is dict
    # TPI-T460  step 4
    def test_api_drivers_clocked_in_locations_data_page_records_driver_status(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_status']) == dict)

    # Drivers clock in location response data_page_records_vehicle_id is dict
    # TPI-T460  step 5
    def test_api_drivers_clocked_in_locations_data_page_records_vehicle_id(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['vehicle_id']) == dict)

    # Drivers clock in location response data_page_records_is_busy is int
    # TPI-T460  step 6
    def test_api_drivers_clocked_in_locations_data_page_records_is_busy(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['is_busy']) == int)

    # Drivers clock in location response data_page_records_driver_orders_count is int
    # TPI-T460  step 7
    def test_api_drivers_clocked_in_locations_data_page_records_driver_orders_count(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_orders_count']) == int)

    # Drivers clock in location response data_page_records_id is int
    # TPI-T460  step 8
    def test_api_drivers_clocked_in_locations_data_page_records_id(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['id']) == int)

    # Drivers clock in location response data_page_records_driver_status_id is int
    # TPI-T460  step 9
    def test_api_drivers_clocked_in_locations_data_page_records_driver_status_id(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_status']['id']) == int)

    # Drivers clock in location response data_page_records_driver_status_name is str
    # TPI-T460  step 10
    def test_api_drivers_clocked_in_locations_data_page_records_driver_status_name(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_status']['name']) == str)

    # Drivers clock in location response data_page_records_driver_status_value is str
    # TPI-T460  step 11
    def test_api_drivers_clocked_in_locations_data_page_records_driver_status_value(self):
        self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_status']['value']) == str)





















































