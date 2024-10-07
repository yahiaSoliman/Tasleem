import random
import string

from API.auth_api import AuthEndPoints
from API.vehicles_api import VehicleAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiDeleteVehicle(BaseApiClass):
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

        # delete vehicle
        global delete_vehicle_response
        delete_vehicle_response = VehicleAPI.delete_vehicle(login_response.json()['data']['access_token'],
                                                            create_vehicle_response.json()['info']['message']['id'])

    def test_code_status(self):
        self.assertEqual(200, delete_vehicle_response.status_code)

    def test_confirmation_message(self):
        self.assertEqual(f"Vehicle with id: {create_vehicle_response.json()['info']['message']['id']} deleted successfully.",
                         delete_vehicle_response.json()['info']['message'])
