import random
import string

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestSetOrderStatusReadyForPickupApi(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        global order_id
        order_id = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))
        response = OrderApis.api_create_auto_assignment_order(order_id, ApiData.dark_store)
        order_id = response.json()['data']['id']
        global set_ready_for_pickup_response
        set_ready_for_pickup_response = OrderApis.set_ready_for_pickup_status(order_id)

    def test_code_status(self):
        self.assertEqual(200, set_ready_for_pickup_response.status_code)

    def test_order_status_changed(self):
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        response = OrderApis.api_get_order_by_id(order_id, login_response.json()['data']['access_token'])
        self.assertEqual('ready_for_pick_up', response.json()['data']['order_status']['name'])
