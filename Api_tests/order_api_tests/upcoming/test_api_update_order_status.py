import random
import string

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestUpdateOrderStatusApi(BaseApiClass):

    @classmethod
    def setUpClass(cls):

        # login
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        # generate order id
        order_id = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))

        # create order
        new_order_response = OrderApis.api_create_auto_assignment_order(order_id, "Stores - TG")

        # set order ready for pickup
        OrderApis.set_ready_for_pickup_status(new_order_response.json()['data']['id'])
        print(new_order_response.json()['data']['id'])
        # assign order manually
        res = OrderApis.assign_order_manually(login_response.json()['data']['access_token'], new_order_response.json()['data']['id'], payload_dict={
            "driver_id": 162,
            "order_sequence": [
                new_order_response.json()['data']['id']
            ],
            "reason_id": 0,
            "note": "string"
        })
        print(res.json())

        global set_picked_up_response
        set_picked_up_response = OrderApis.update_order_status(login_response.json()['data']['access_token'],
                                                               new_order_response.json()['data']['id'])

    def test_code_status(self):
        print(set_picked_up_response.json())
        self.assertEqual(200, set_picked_up_response.status_code)

    def test_order_status(self):
        self.assertEqual("picked_up", set_picked_up_response.json()['data']['order_status']['name'])
