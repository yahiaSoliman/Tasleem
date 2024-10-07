import random
import string

from API.auth_api import AuthEndPoints
from API.vehicles_api import VehicleAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiGetVehicle(BaseApiClass):
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
        # get vehicle
        global get_vehicle_response
        get_vehicle_response = VehicleAPI.get_vehicle(login_response.json()['data']['access_token'],
                                                      create_vehicle_response.json()['info']['message']['id'])

    def test_status_code(self):
        self.assertEqual(200, get_vehicle_response.status_code)

    def test_vehicle_name(self):
        self.assertEqual("testName", get_vehicle_response.json()['data']['name'])

    def test_vehicle_model(self):
        self.assertEqual("2101", get_vehicle_response.json()['data']['model'])

    def test_vehicle_make(self):
        self.assertEqual("testMake", get_vehicle_response.json()['data']['make'])

    def test_vehicle_year(self):
        self.assertEqual("1960", get_vehicle_response.json()['data']['year'])

    def test_vehicle_license_no(self):
        self.assertEqual(license_number, get_vehicle_response.json()['data']['license_no'])

    def test_vehicle_type_id(self):
        self.assertEqual(1, get_vehicle_response.json()['data']['vehicle_type']['id'])

    def test_vehicle_owner(self):
        self.assertEqual("driver", get_vehicle_response.json()['data']['owner'])

    def test_vehicle_id_type(self):
        self.assertEqual(int, type(get_vehicle_response.json()['data']['id']))

    def test_vehicle_is_active_flag(self):
        self.assertEqual(True, get_vehicle_response.json()['data']['is_activated'])

    def test_vehicle_is_assigned_flag(self):
        self.assertEqual(False, get_vehicle_response.json()['data']['is_assigned'])
