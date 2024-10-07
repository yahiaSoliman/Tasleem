import random
import string

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestGetOrderApi(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        global access_token
        access_token = response_a.json()['data']['access_token']

        global order_id
        order_id = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))
        global create_order_response
        global darkstore
        darkstore = ApiData.dark_store
        create_order_response = OrderApis.api_create_auto_assignment_order(order_id, darkstore)

        global get_order_response
        get_order_response = OrderApis.api_get_order_by_id(order_id, access_token)

    def test_status_code(self):
        self.assertEqual(200, get_order_response.status_code)

    def test_destination_latitude(self):
        self.assertEqual(33.310081, get_order_response.json()['data']['destination_latitude'])

    def test_destination_longitude(self):
        self.assertEqual(44.36919, get_order_response.json()['data']['destination_longitude'])

    def test_order_bin_info(self):
        self.assertEqual(123, get_order_response.json()['data']['order_bin_info'][0]['324234'])
        self.assertEqual(123, get_order_response.json()['data']['order_bin_info'][1]['42'])

    def test_customer_code(self):
        self.assertEqual("1111", get_order_response.json()['data']['customer_code'])

    def test_order_id(self):
        self.assertEqual(order_id, get_order_response.json()['data']['order_id'])

    def test_darkstore_name(self):
        self.assertEqual(ApiData.dark_store, get_order_response.json()['data']['dark_store']['name'])

    def test_user_address(self):
        self.assertEqual("yahia address", get_order_response.json()['data']['user_address'])

    def test_vehicle_type_value(self):
        self.assertEqual("Motor", get_order_response.json()['data']['vehicle_type']['value'])

    def test_vehicle_type_name(self):
        self.assertEqual("motor", get_order_response.json()['data']['vehicle_type']['name'])

    def test_vehicle_type_id(self):
        self.assertEqual(2, get_order_response.json()['data']['vehicle_type']['id'])

    def test_order_total(self):
        self.assertEqual("2100", get_order_response.json()['data']['order_total'])

    def test_customer_phone_number(self):
        self.assertEqual("+4232423423", get_order_response.json()['data']['customer_phone_number'])

    def test_address_flat(self):
        self.assertEqual("test_flat", get_order_response.json()['data']['customer_address_details']['address_flat'])

    def test_address_floor(self):
        self.assertEqual("test_floor", get_order_response.json()['data']['customer_address_details']['address_floor'])

    def test_address_phone(self):
        self.assertEqual("test_address_phone", get_order_response.json()['data']['customer_address_details']['address_phone'])

    def test_address_building(self):
        self.assertEqual("test_building",
                         get_order_response.json()['data']['customer_address_details']['address_building'])

    def test_address_district(self):
        self.assertEqual("test_district", get_order_response.json()['data']['customer_address_details']['address_district'])

    def test_address_neighbourhood(self):
        self.assertEqual("test_neighbourhood",
                         get_order_response.json()['data']['customer_address_details']['address_neighbourhood'])

    def test_address_nickname(self):
        self.assertEqual("test_nickname", get_order_response.json()['data']['customer_address_details']['address_nickname'])

    def test_address_address_line1(self):
        self.assertEqual("test_address_line1",
                         get_order_response.json()['data']['customer_address_details']['address_address_line1'])
