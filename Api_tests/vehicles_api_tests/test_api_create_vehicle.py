import random
import string

from API.auth_api import AuthEndPoints
from API.vehicles_api import VehicleAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiCreateVehicle(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        # generate vehicle licence number
        global license_number
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

    def test_status_code(self):
        self.assertEqual(200, create_vehicle_response.status_code)

    def test_vehicle_name(self):
        self.assertEqual("testName", create_vehicle_response.json()['info']['message']['name'])

    def test_vehicle_model(self):
        self.assertEqual("2101", create_vehicle_response.json()['info']['message']['model'])

    def test_vehicle_make(self):
        self.assertEqual("testMake", create_vehicle_response.json()['info']['message']['make'])

    def test_vehicle_year(self):
        self.assertEqual("1960", create_vehicle_response.json()['info']['message']['year'])

    def test_vehicle_license_no(self):
        self.assertEqual(license_number, create_vehicle_response.json()['info']['message']['license_no'])

    def test_vehicle_type_id(self):
        self.assertEqual(1, create_vehicle_response.json()['info']['message']['vehicle_type']['id'])

    def test_vehicle_owner(self):
        self.assertEqual("driver", create_vehicle_response.json()['info']['message']['owner'])

    def test_vehicle_id_type(self):
        self.assertEqual(int, type(create_vehicle_response.json()['info']['message']['id']))

    def test_vehicle_is_active_flag(self):
        self.assertEqual(True, create_vehicle_response.json()['info']['message']['is_activated'])

    def test_vehicle_is_assigned_flag(self):
        self.assertEqual(False, create_vehicle_response.json()['info']['message']['is_assigned'])
