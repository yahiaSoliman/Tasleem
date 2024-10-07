from unittest import skip

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestGelAllOrdersApi(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global response_a
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        global response
        response = OrderApis.get_all_orders(response_a.json()['data']['access_token'], Qparams={
            'per_page': 2,
            'page_number': 1
        }, timeout=15)

    def test_status_code(self):
        self.assertEqual(200, response.status_code)

    def test_pagination(self):
        self.assertEqual(2, response.json()['data']['per_page'])
        self.assertEqual(1, response.json()['data']['current_page'])
        self.assertEqual(2, len(response.json()['data']['page_records']))

    def test_priority_exists(self):
        self.assertTrue('priority' in response.json()['data']['page_records'][0])

    def test_order_bin_info_type(self):
        self.assertEqual(list, type(response.json()['data']['page_records'][0]['order_bin_info']))

    def test_coordinates_type(self):
        self.assertEqual(float, type(response.json()['data']['page_records'][0]['destination_longitude']))
        self.assertEqual(float, type(response.json()['data']['page_records'][0]['destination_latitude']))

    def test_order_total_type(self):
        self.assertEqual(str, type(response.json()['data']['page_records'][0]['order_total']))

    def test_customer_address_details_type(self):
        self.assertEqual(dict, type(response.json()['data']['page_records'][0]['customer_address_details']))

    def test_order_status_time_type(self):
        self.assertEqual(list, type(response.json()['data']['page_records'][0]['order_status_time']))

    def test_bin_number_type(self):
        self.assertEqual(str, type(response.json()['data']['page_records'][0]['order_bin_number']))

    def test_zone_type(self):
        self.assertTrue('zone' in response.json()['data']['page_records'][0])

    def test_order_id_type(self):
        self.assertEqual(str, type(response.json()['data']['page_records'][0]['order_id']))

    def test_id_type(self):
        self.assertEqual(int, type(response.json()['data']['page_records'][0]['id']))

    def test_vehicle_type(self):
        self.assertEqual(dict, type(response.json()['data']['page_records'][0]['vehicle_type']))

    def test_customer_code(self):
        self.assertEqual(str, type(response.json()['data']['page_records'][0]['customer_code']))

    def test_deliver_first_type(self):
        self.assertEqual(bool, type(response.json()['data']['page_records'][0]['is_to_deliver_first']))

    def test_creation_date_type(self):
        self.assertEqual(str, type(response.json()['data']['page_records'][0]['created_at']))

    def test_order_status_id_type(self):
        self.assertEqual(int, type(response.json()['data']['page_records'][0]['order_status_id']))

    def test_order_status_type(self):
        self.assertEqual(dict, type(response.json()['data']['page_records'][0]['order_status']))

    def test_user_address_type(self):
        self.assertEqual(str, type(response.json()['data']['page_records'][0]['user_address']))

    def test_dark_store_type(self):
        self.assertEqual(dict, type(response.json()['data']['page_records'][0]['dark_store']))

    def test_zone_id_type(self):
        self.assertTrue('zone_id' in response.json()['data']['page_records'][0])

    @skip("too long response time")
    def test_search(self):
        order_id = response.json()['data']['page_records'][0]['order_id']
        search_response = OrderApis.get_all_orders(response_a.json()['data']['access_token'], Qparams={
            'per_page': 2,
            'page_number': 1,
            'search': order_id
        }, timeout=(5, 5))
        self.assertEqual(1, len(search_response.json()['data']['page_records']))
        self.assertEqual(order_id, search_response.json()['data']['page_records'][0]['order_id'])
