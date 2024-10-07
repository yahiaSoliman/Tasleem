import random
import string

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestCancelOrderApi(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # create order
        global order_id
        order_id = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))
        response_a = OrderApis.api_create_auto_assignment_order(order_id, darkstore=ApiData.dark_store)

        # cancel order
        global response_b
        response_b = OrderApis.cancel_order(order_id, default)

    def test_status_code(self):
        self.assertEqual(200, response_b.status_code)

    def test_cancel_confirmation_message(self):
        self.assertEqual("Order with id: " + order_id + " has been cancelled successfully",
                         response_b.json()['info']['message'])

    def test_order_status(self):
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        response_c = OrderApis.api_get_order_by_id(order_id, response_a.json()['data']['access_token'])
        self.assertEqual('canceled', response_c.json()['data']['order_status']['name'])

    def test_already_cancelled_order_message(self):
        response = OrderApis.cancel_order(order_id, default)
        self.assertEqual("Order with id: " + order_id + " is already canceled", response.json()['info']['message'])
