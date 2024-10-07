import random
import string

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiOrderDetails(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        global order_id
        order_id = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))
        global response_b
        global  darkstore
        darkstore = ApiData.dark_store
        create_order_response = OrderApis.api_create_auto_assignment_order(order_id, darkstore)

        # get order details
        global get_order_details_response
        get_order_details_response = OrderApis.get_order_details(access_token, order_id)

    def test_code_status(self):
        self.assertEqual(200, get_order_details_response.status_code)

    def test_id_type(self):
        self.assertEqual(int, type(get_order_details_response.json()['data']['id']))

    def test_is_to_deliver_first_type(self):
        self.assertEqual(bool, type(get_order_details_response.json()['data']['is_to_deliver_first']))

    def test_order_id(self):
        self.assertEqual(order_id, get_order_details_response.json()['data']['order_id'])

    def test_order_total(self):
        self.assertEqual("2100", get_order_details_response.json()['data']['order_total'])

    def test_priority_type(self):
        self.assertEqual(bool, type(get_order_details_response.json()['data']['priority']))

    def test_driver_object_type(self):
        self.assertEqual(dict, type(get_order_details_response.json()['data']['driver']))

    def test_order_status_name(self):
        self.assertEqual("preparing", get_order_details_response.json()['data']['order_status']['name'])

    def test_order_status_value(self):
        self.assertEqual("Preparing", get_order_details_response.json()['data']['order_status']['value'])

    def test_order_status_id(self):
        self.assertEqual(1, get_order_details_response.json()['data']['order_status']['id'])

    def test_preparing_status(self):
        self.assertEqual("preparing", get_order_details_response.json()['data']['order_status_time'][0]['status'])

