from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiAutocompleteAttributeValues(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        global response_a
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        global response_b
        response_b = OrderApis.order_autocomplete(response_a.json()['data']['access_token'], Qparams={
            "page_number": 1,
            "per_page": 10,
            "query": "green170"
        })

    def test_order_id_value(self):
        self.assertEqual("green170", response_b.json()['data']['page_records'][0]['order_id'])

    def test_driver_id_value(self):
        self.assertEqual(162, response_b.json()['data']['page_records'][0]['driver_id'])

    def test_date_range_from_value(self):
        self.assertEqual("2023-11-24T14:07:28", response_b.json()['data']['page_records'][0]['date_range_from'])

    def test_date_range_to_value(self):
        self.assertEqual("2023-11-24T14:11:03", response_b.json()['data']['page_records'][0]['date_range_to'])

    def test_username_value(self):
        self.assertEqual("catN", response_b.json()['data']['page_records'][0]['username'])

    def test_id_value(self):
        self.assertEqual(4530, response_b.json()['data']['page_records'][0]['id'])
