from API.auth_api import AuthEndPoints
from API.vehicles_api import VehicleAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiGetAllVehicleTypes(BaseApiClass):

    @classmethod
    def setUpClass(cls):

        # get all vehicle types
        global all_vehicles_response
        all_vehicles_response = VehicleAPI.get_all_vehicle_types()

    def test_code_status(self):
        self.assertEqual(200, all_vehicles_response.status_code)

    def test_car_vehicle(self):
        output = [x for x in all_vehicles_response.json()['data'] if x['name'] == "car"]

        self.assertEqual("car", output[0]['name'])
        self.assertEqual(1, output[0]['id'])
        self.assertEqual("Car", output[0]['value'])

    def test_car_motor(self):
        output = [x for x in all_vehicles_response.json()['data'] if x['name'] == "motor"]

        self.assertEqual("motor", output[0]['name'])
        self.assertEqual(2, output[0]['id'])
        self.assertEqual("Motor", output[0]['value'])

    def test_car_bicycle(self):
        output = [x for x in all_vehicles_response.json()['data'] if x['name'] == "bicycle"]

        self.assertEqual("bicycle", output[0]['name'])
        self.assertEqual(3, output[0]['id'])
        self.assertEqual("Bicycle", output[0]['value'])



