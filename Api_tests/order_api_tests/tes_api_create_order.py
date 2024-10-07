import random
import string

from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestCreateOrderApi(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        global order_id
        order_id = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))
        global response_b
        global  darkstore
        darkstore = ApiData.dark_store
        response_b = OrderApis.api_create_auto_assignment_order(order_id, darkstore)

    def test_status_code(self):
        # print(response_b.json())
        self.assertEqual(200, response_b.status_code)

    def test_order_status(self):
        self.assertEqual("preparing", response_b.json()['data']['order_status']['name'])

    def test_vehicle_type_value(self):
        self.assertEqual("Motor", response_b.json()['data']['vehicle_type']['value'])

    def test_vehicle_type_name(self):
        self.assertEqual("motor", response_b.json()['data']['vehicle_type']['name'])

    def test_vehicle_type_id(self):
        self.assertEqual("motor", response_b.json()['data']['vehicle_type']['name'])

    def test_order_bin_info(self):
        self.assertEqual(123, response_b.json()['data']['order_bin_info'][0]['324234'])
        self.assertEqual(123, response_b.json()['data']['order_bin_info'][1]['42'])

    def test_destination_latitude(self):
        self.assertEqual(33.310081, response_b.json()['data']['destination_latitude'])

    def test_destination_longitude(self):
        self.assertEqual(44.36919, response_b.json()['data']['destination_longitude'])

    def test_order_total(self):
        self.assertEqual("2100", response_b.json()['data']['order_total'])

    def test_customer_address_flat(self):
        self.assertEqual("test_flat", response_b.json()['data']['customer_address_details']['address_flat'])

    def test_address_floor(self):
        self.assertEqual("test_floor", response_b.json()['data']['customer_address_details']['address_floor'])

    def test_address_phone(self):
        self.assertEqual("test_address_phone", response_b.json()['data']['customer_address_details']['address_phone'])

    def test_address_building(self):
        self.assertEqual("test_building",
                         response_b.json()['data']['customer_address_details']['address_building'])

    def test_address_district(self):
        self.assertEqual("test_district", response_b.json()['data']['customer_address_details']['address_district'])

    def test_address_neighbourhood(self):
        self.assertEqual("test_neighbourhood",
                         response_b.json()['data']['customer_address_details']['address_neighbourhood'])

    def test_address_nickname(self):
        self.assertEqual("test_nickname", response_b.json()['data']['customer_address_details']['address_nickname'])

    def test_address_address_line1(self):
        self.assertEqual("test_address_line1",
                         response_b.json()['data']['customer_address_details']['address_address_line1'])

    def test_customer_phone_number(self):
        self.assertEqual("+4232423423", response_b.json()['data']['customer_phone_number'])

    def test_customer_code(self):
        self.assertEqual("1111", response_b.json()['data']['customer_code'])

    def test_user_address(self):
        self.assertEqual("yahia address", response_b.json()['data']['user_address'])

    def test_order_id(self):
        self.assertEqual(order_id, response_b.json()['data']['order_id'])

    def test_order_bin_number(self):
        self.assertEqual("123456", response_b.json()['data']['order_bin_number'])

    def test_darkstore_name(self):
        self.assertEqual(darkstore, response_b.json()['data']['dark_store']['name'])
