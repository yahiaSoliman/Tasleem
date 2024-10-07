from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriverStatusUpdatesPage(BaseApiClass):

    def setUp(self):
        super().setUp()
        global superadmintoken
        global drivers_driver_status_updates_all
        superadmintoken = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password).json()['data'].get('access_token')
        drivers_driver_status_updates_all = DriverEndPoints.api_driver_status_updates_page(self.BASE_URL, superadmintoken, params={})

    # Drivers page response with 200
    #   step 1
    def test_api_drivers_driver_status_updates_all(self):
        self.assertTrue(drivers_driver_status_updates_all.status_code == 200)

    # Drivers driver status updates all response data is dist
    #   step 2
    def test_api_drivers_driver_status_updates_all_data(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']) == dict)

    # Drivers driver status updates all response data_num_records is int
    #   step 3
    def test_api_drivers_driver_status_updates_all_data_num_records(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['num_records']) == int)

    # Drivers driver status updates all response data_page_records is list
    #  step 4
    def test_api_drivers_driver_status_updates_all_data_page_records(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records']) == list)

    # Drivers driver status updates all response data_per_page is int
    #   step 5
    def test_api_drivers_driver_status_updates_all_data_per_page(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['per_page']) == int)

    # Drivers driver status updates all response data_current_page is int
    #   step 6
    def test_api_drivers_driver_status_updates_all_data_current_page(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['current_page']) == int)

    # Drivers driver status updates all response data_num_pages is int
    #   step 7
    def test_api_drivers_driver_status_updates_all_data_num_pages(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['num_pages']) == int)

    # Drivers driver status updates all response data_page_records_id is int
    #   step 8
    def test_api_drivers_driver_status_updates_all_data_page_records_id(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['id']) == int)

    # Drivers driver status updates all response data_page_records_is_clock_in is bool
    #   step 9
    def test_api_drivers_driver_status_updates_all_data_page_records_is_clock_in(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['is_clock_in']) == bool)

    # Drivers driver status updates all response data_page_records_is_busy is int
    #   step 10
    def test_api_drivers_driver_status_updates_all_data_page_records_is_busy(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['is_busy']) == int)

    # Drivers driver status updates all response data_page_records_license is str
    #  step 11
    def test_api_drivers_driver_status_updates_all_data_page_records_license(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['license']) == str)

    # Drivers driver status updates all response data_page_records_box_number is str
    #   step 12
    def test_api_drivers_driver_status_updates_all_data_page_records_box_number(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['box_number']) == str)

    # Drivers driver status updates all response data_page_records_driver_license_no is str
    #   step 13
    def test_api_drivers_driver_status_updates_all_data_page_records_driver_license_no(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['driver_license_no']) == str)

    # Drivers driver status updates all response data_page_records_created_at is str
    #   step 14
    def test_api_drivers_driver_status_updates_all_data_page_records_created_at(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['created_at']) == str)

    # Drivers driver status updates all response data_page_records_darkstore is dict
    #  step 15
    def test_api_drivers_driver_status_updates_all_data_page_records_darkstore(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['darkstore']) == dict)

    # Drivers driver status updates all response data_page_records_driver_address is dict
    #   step 16
    def test_api_drivers_driver_status_updates_all_data_page_records_driver_address(self):
        self.assertTrue(type(drivers_driver_status_updates_all.json()['data']['page_records'][0]['driver_address']) == dict)
