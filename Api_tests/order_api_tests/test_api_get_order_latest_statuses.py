import random
import string

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestGetOrderLatestStatuses(BaseApiClass):

    @classmethod
    def setUpClass(cls):

        # login
        global response_a
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        # generate random ids
        global order_id_1
        order_id_1 = ''.join(random.choices(string.ascii_lowercase +
                                            string.digits, k=7))
        global order_id_2
        order_id_2 = ''.join(random.choices(string.ascii_lowercase +
                                            string.digits, k=7))
        # create orders
        OrderApis.api_create_auto_assignment_order(order_id_1, ApiData.dark_store)
        OrderApis.api_create_auto_assignment_order(order_id_2, ApiData.dark_store)

        # get latest order statuses
        global response_b
        response_b = OrderApis.get_order_latest_statuses(response_a.json()['data']['access_token'],
                                                         [order_id_1, order_id_2])

    def test_code_status(self):
        self.assertEqual(200, response_b.status_code)

    def test_first_order_status(self):
        output = [x for x in response_b.json()['data'] if x['order_id'] == order_id_1]
        self.assertEqual("preparing", output[0]['order_status']['name'])

    def test_second_order_status(self):
        output = [x for x in response_b.json()['data'] if x['order_id'] == order_id_2]
        self.assertEqual("preparing", output[0]['order_status']['name'])

    def test_first_order_updated_status(self):
        OrderApis.cancel_order(order_id_1, default)
        response = OrderApis.get_order_latest_statuses(response_a.json()['data']['access_token'], [order_id_1])
        self.assertEqual("canceled", response.json()['data'][0]['order_status']['name'])

    def test_second_order_updated_status(self):
        OrderApis.cancel_order(order_id_2, default)
        response = OrderApis.get_order_latest_statuses(response_a.json()['data']['access_token'], [order_id_2])
        self.assertEqual("canceled", response.json()['data'][0]['order_status']['name'])
