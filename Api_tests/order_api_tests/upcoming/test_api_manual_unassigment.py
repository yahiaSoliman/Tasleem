from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiManualUnassigment(BaseApiClass):

    @classmethod
    def setUpClass(cls) -> None:
        # login
        global response_a
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        # get all orders
        global response_b
        response_b = OrderApis.unassign_order_manually(response_a.json()['data']['access_token'], 5384, payload_dict={
            "order_sequence": [
                5384
            ],
            "await_further_orders": 1,
            "reason_id": 0,
            "note": "string"
        })

    def test_code_status(self):
        print(response_b.json())
        self.assertEqual(200, response_b.status_code)

    def test_order_status(self):
        self.assertEqual("ready_for_pick_up", response_b.json()['data']['order_status']['name'])

    def test_driver_info(self):
        self.assertEqual(None, response_b.json()['data']['driver'])



