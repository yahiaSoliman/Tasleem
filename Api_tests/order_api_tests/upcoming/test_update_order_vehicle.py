import random
import string

from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiUpdateOrderVehicle(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global response_a
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        global order_id
        order_id = ''.join(random.choices(string.ascii_lowercase +
                                          string.digits, k=7))

        response_b = OrderApis.api_create_auto_assignment_order(order_id, "Stores - TG")

        global order_numeric_id
        order_numeric_id = response_b.json()['data']['id']

    def test_vehicle_updated_when_status_preparing(self):
        response = OrderApis.api_get_order_by_id(order_id, response_a.json()['data']['access_token'])
        self.assertEqual(2, response.json()['data']['vehicle_type']['id'])

        response = OrderApis.update_order_vehicle(response_a.json()['data']['access_token'],
                                                  order_numeric_id, 1)
        self.assertEqual(f"Order: {order_numeric_id} vehicle type updated successfully",
                         response.json()['info']['message'])

        response = OrderApis.api_get_order_by_id(order_id, response_a.json()['data']['access_token'])
        self.assertEqual(1, response.json()['data']['vehicle_type']['id'])

    def test_vehicle_updated_when_status_ready_for_pickup(self):
        response = OrderApis.set_ready_for_pickup_status(order_id)
        self.assertEqual(200, response.status_code)

        response = OrderApis.update_order_vehicle(response_a.json()['data']['access_token'],
                                                  order_numeric_id, 3)
        self.assertEqual(f"Order: {order_numeric_id} vehicle type updated successfully",
                         response.json()['info']['message'])

        response = OrderApis.api_get_order_by_id(order_id, response_a.json()['data']['access_token'])
        self.assertEqual(3, response.json()['data']['vehicle_type']['id'])

    # verify that admin can't update order vehicle if order is assigned to driver
    def test_vehicle_not_updated_when_order_assigned(self):

        response = OrderApis.update_order_vehicle(response_a.json()['data']['access_token'],
                                                  4530, 2)
        self.assertEqual("Order has driver assigned, you should first unassign the driver",
                         response.json()['info']['message'])


