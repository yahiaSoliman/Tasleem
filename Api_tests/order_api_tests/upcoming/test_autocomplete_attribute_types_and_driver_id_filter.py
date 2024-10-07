from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiAutocompleteResponseAttributeTypes(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        global response_c
        response_c = OrderApis.order_autocomplete(response_a.json()['data']['access_token'], Qparams={
            "page_number": 1,
            "per_page": 10,
            "driver_id": 162
        })

    def test_type_of_order_id(self):
        self.assertEqual(str, type(response_c.json()['data']['page_records'][0]['order_id']))

    def test_type_of_driver_id(self):
        self.assertEqual(int, type(response_c.json()['data']['page_records'][0]['driver_id']))

    def test_type_of_username(self):
        self.assertEqual(str, type(response_c.json()['data']['page_records'][0]['username']))

    def test_type_of_id(self):
        self.assertEqual(int, type(response_c.json()['data']['page_records'][0]['id']))

    def test_type_of_date_range_from(self):
        self.assertEqual(str, type(response_c.json()['data']['page_records'][0]['date_range_from']))

    def test_type_of_date_range_to(self):
        self.assertEqual(str, type(response_c.json()['data']['page_records'][0]['date_range_to']))

    def test_driver_id_filter(self):
        for x in response_c.json()['data']['page_records']:
            self.assertEqual(162, x['driver_id'])
