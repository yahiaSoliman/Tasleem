import random
import string

from API.auth_api import AuthEndPoints
from API.vehicles_api import VehicleAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiActivateVehicle(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global login_response
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        # generate vehicle licence number
        license_number = ''.join(random.choices(string.ascii_lowercase +
                                                string.digits, k=7))

        # create vehicle
        global create_vehicle_response
        create_vehicle_response = VehicleAPI.create_vehicle(login_response.json()['data']['access_token'],
                                                            payload_dict={
                                                                "name": "testName",
                                                                "model": "2101",
                                                                "make": "testMake",
                                                                "year": 1960,
                                                                "license_no": license_number,
                                                                "vehicle_type_id": 1,
                                                                "owner": "driver"
                                                            })

    def test_a_activate_activated_vehicle(self):
        response = VehicleAPI.activate_vehicle(login_response.json()['data']['access_token'],
                                               create_vehicle_response.json()['info']['message']['id'],
                                               1)
        self.assertEqual(
            f"Vehicle with id: {create_vehicle_response.json()['info']['message']['id']} is already activated",
            response.json()['info']['message'])

    def test_b_deactivate_vehicle(self):
        response = VehicleAPI.activate_vehicle(login_response.json()['data']['access_token'],
                                               create_vehicle_response.json()['info']['message']['id'],
                                               0)
        self.assertEqual(False,
                         response.json()['info']['message']['is_activated'])

    def test_c_deactivate_deactivated_vehicle(self):
        VehicleAPI.activate_vehicle(login_response.json()['data']['access_token'],
                                    create_vehicle_response.json()['info']['message']['id'],
                                    0)
        response = VehicleAPI.activate_vehicle(login_response.json()['data']['access_token'],
                                               create_vehicle_response.json()['info']['message']['id'],
                                               0)
        self.assertEqual(
            f"Vehicle with id: {create_vehicle_response.json()['info']['message']['id']} is already deactivated",
            response.json()['info']['message'])

    def test_d_activate_vehicle(self):
        response = VehicleAPI.activate_vehicle(login_response.json()['data']['access_token'],
                                               create_vehicle_response.json()['info']['message']['id'],
                                               1)
        self.assertEqual(True,
                         response.json()['info']['message']['is_activated'])
