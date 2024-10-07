from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriversSearchAutocomplete(BaseApiClass):

    def setUp(self):
        super().setUp()
        global superadmintoken
        global drivers_search_autocomplete_res
        superadmintoken = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password).json()[ 'data'].get('access_token')
        drivers_search_autocomplete_res = DriverEndPoints.api_drivers_search_autocomplete(self.BASE_URL, superadmintoken, search='', per_page='10', page='1')

    # Drivers search autocomplete response with 200
    # TPI-T456  step 1
    def test_api_search_autocomplete_statuscode(self):
        self.assertTrue(drivers_search_autocomplete_res.status_code == 200)

    # Drivers search autocomplete response data is dist
    # TPI-T456  step 2
    def test_api_drivers_search_autocomplete_data(self):
        self.assertTrue(type(drivers_search_autocomplete_res.json()['data']) == dict)

    # Drivers search autocomplete response data_num_records is int
    # TPI-T456  step 3
    def test_api_drivers_search_autocomplete_data_num_records(self):
        self.assertTrue(type(drivers_search_autocomplete_res.json()['data']['num_records']) == int)

    # Drivers search autocomplete response data_page_records is list
    # TPI-T456  step 4
    def test_api_drivers_search_autocomplete_data_page_records(self):
        self.assertTrue(type(drivers_search_autocomplete_res.json()['data']['page_records']) == list)

    # Drivers search autocomplete response data_per_page is int
    # TPI-T456  step 5
    def test_api_drivers_search_autocomplete_data_per_page(self):
        self.assertTrue(type(drivers_search_autocomplete_res.json()['data']['per_page']) == int)

    # Drivers search autocomplete response data_current_page is int
    # TPI-T456  step 6
    def test_api_drivers_search_autocomplete_data_current_page(self):
        self.assertTrue(type(drivers_search_autocomplete_res.json()['data']['current_page']) == int)

    # Drivers search autocomplete response data_num_pages is int
    # TPI-T456  step 7
    def test_api_drivers_search_autocomplete_data_num_pages(self):
        self.assertTrue(type(drivers_search_autocomplete_res.json()['data']['num_pages']) == int)

    # Drivers search autocomplete response data_page_records_driver_id is int
    # TPI-T456  step 8
    def test_api_drivers_page_search_autocomplete_page_records_driver_id(self):
        self.assertTrue(type(drivers_search_autocomplete_res.json()['data']['page_records'][0]['driver_id']) == int)

    # Drivers search autocomplete response data_page_records_username is str
    # TPI-T456  step 8
    def test_api_drivers_page_search_autocomplete_page_records_username(self):
        self.assertTrue(type(drivers_search_autocomplete_res.json()['data']['page_records'][0]['username']) == str)


class APIDriverDriversSearchAutocompleteSearch(BaseApiClass):

    def setUp(self):
        super().setUp()
        global superadmintoken
        global drivers_search_autocomplete_res
        superadmintoken = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password).json()['data'].get('access_token')
        drivers_search_autocomplete_res = DriverEndPoints.api_drivers_search_autocomplete(self.BASE_URL, superadmintoken, search='aromanii', per_page='10', page='1')

    # Drivers search autocomplete search response with 200
    # TPI-T459  step 1
    def test_api_search_autocomplete_search_statuscode(self):
        self.assertTrue(drivers_search_autocomplete_res.status_code == 200)

    # Drivers search autocomplete search response data_page_records_username equals to "aromanii"
    # TPI-T459  step 2
    def test_api_drivers_page_search_autocomplete_search_page_records_username(self):
        self.assertEqual(drivers_search_autocomplete_res.json()['data']['page_records'][0]['username'], 'aromanii')

    # Drivers search autocomplete search response data_page_records_driver_id equals to 9
    # TPI-T459  step 3
    def test_api_drivers_page_search_autocomplete_search_page_records_driver_id(self):
        self.assertEqual(drivers_search_autocomplete_res.json()['data']['page_records'][0]['driver_id'], 9)






























