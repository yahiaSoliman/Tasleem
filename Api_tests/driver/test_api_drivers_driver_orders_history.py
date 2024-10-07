from core.api_data import ApiData
from core.data_sets import DataSets
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriverOrdersHistory(BaseApiClass):

    def setUp(self):
        super().setUp()
        from_date = DataSets.from_date()
        to_date = DataSets.to_date()
        global driver_token
        global driver_orders_history_res
        driver_token = AuthEndPoints.api_login(self.BASE_URL, ApiData.driver_username, ApiData.driver_password).json()['data'].get('access_token')
        driver_orders_history_res = DriverEndPoints.api_driver_orders_history(self.BASE_URL, driver_token, params={'from_date': from_date,
                                                                                                                   'to_date': to_date})

    # Driver orders history response with 200
    #   step 1
    def test_api_driver_orders_history_statuscode(self):
        self.assertTrue(driver_orders_history_res.status_code == 200)

    # Driver orders history response data is dist
    #  step 2
    def test_api_driver_orders_history_data(self):
        self.assertTrue(type(driver_orders_history_res.json()['data']) == dict)

    # DDriver orders history response data_page_records is list
    #   step 3
    def test_api_driver_orders_history_data_page_records(self):
        self.assertTrue(type(driver_orders_history_res.json()['data']['page_records']) == list)

    # DDriver orders history response data_num_records is list
    #   step 3
    def test_api_driver_orders_history_data_num_records(self):
        self.assertTrue(type(driver_orders_history_res.json()['data']['num_records']) == int)

    # DDriver orders history response data_per_page is list
    #   step 3
    def test_api_driver_orders_history_data_per_page(self):
        self.assertTrue(type(driver_orders_history_res.json()['data']['per_page']) == int)

    # DDriver orders history response data_current_page is list
    #   step 3
    def test_api_driver_orders_history_data_current_page(self):
        self.assertTrue(type(driver_orders_history_res.json()['data']['current_page']) == int)

    # DDriver orders history response data_orders_total is list
    #   step 3
    def test_api_driver_orders_history_data_orders_total(self):
        self.assertTrue(type(driver_orders_history_res.json()['data']['orders_total']) == int)

    # DDriver orders history response data_page_records_customer_code is int
    #   step 3
    def test_api_driver_orders_history_data_page_records_customer_code(self):
        print(driver_orders_history_res.status_code)
        print(driver_orders_history_res.json())
        self.assertTrue(type(driver_orders_history_res.json()['data']['page_records'][0]['customer_code']) == int)


    # # Driver orders history response data_page_records_driver_status is dict
    # # TPI-T460  step 4
    # def test_api_driver_orders_history_data_page_records_driver_status(self):
    #     self.assertTrue(type(driver_orders_history_res.json()['data']['page_records'][0]['driver_status']) == dict)

    # # Driver orders history response data_page_records_vehicle_id is dict
    # # TPI-T460  step 5
    # def test_api_drivers_clocked_in_locations_data_page_records_vehicle_id(self):
    #     self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['vehicle_id']) == dict)
    #
    # # Drivers clock in location response data_page_records_is_busy is int
    # # TPI-T460  step 6
    # def test_api_drivers_clocked_in_locations_data_page_records_is_busy(self):
    #     self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['is_busy']) == int)
    #
    # # Drivers clock in location response data_page_records_driver_orders_count is int
    # # TPI-T460  step 7
    # def test_api_drivers_clocked_in_locations_data_page_records_driver_orders_count(self):
    #     self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_orders_count']) == int)
    #
    # # Drivers clock in location response data_page_records_id is int
    # # TPI-T460  step 8
    # def test_api_drivers_clocked_in_locations_data_page_records_id(self):
    #     self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['id']) == int)
    #
    # # Drivers clock in location response data_page_records_driver_status_id is int
    # # TPI-T460  step 9
    # def test_api_drivers_clocked_in_locations_data_page_records_driver_status_id(self):
    #     self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_status']['id']) == int)
    #
    # # Drivers clock in location response data_page_records_driver_status_name is str
    # # TPI-T460  step 10
    # def test_api_drivers_clocked_in_locations_data_page_records_driver_status_name(self):
    #     self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_status']['name']) == str)
    #
    # # Drivers clock in location response data_page_records_driver_status_value is str
    # # TPI-T460  step 11
    # def test_api_drivers_clocked_in_locations_data_page_records_driver_status_value(self):
    #     self.assertTrue(type(drivers_clocked_in_locations_res.json()['data']['page_records'][0]['driver_status']['value']) == str)



