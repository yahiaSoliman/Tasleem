import random
import string
import time

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestManualAssignmentApi(BaseApiClass):

    @classmethod
    def setUpClass(cls) -> None:
        # login
        global login_response
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        # generate order id
        order_id = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))

        # create order
        new_order_response = OrderApis.api_create_auto_assignment_order(order_id, "Stores - TG")

        # assign order
        global response_b
        response_b = OrderApis.assign_order_manually(login_response.json()['data']['access_token'],
                                                     new_order_response.json()
                                                     ['data']['id'], payload_dict={
                "driver_id": 162,
                "order_sequence": [
                    new_order_response.json()['data']['id']
                ],
                "reason_id": 0,
                "note": "string"
            })

    def test_code_status(self):
        print(response_b.json())
        self.assertEqual(200, response_b.status_code)

    def test_order_status(self):
        self.assertEqual("assigned", response_b.json()['data']['order_status']['name'])

    def test_driver_info(self):
        self.assertEqual(162, response_b.json()['data']['driver']['id'])
