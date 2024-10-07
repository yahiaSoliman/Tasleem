from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiAutocompletePagination(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        global response_a
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

    def test_one_item_per_page(self):
        response_b = OrderApis.order_autocomplete(response_a.json()['data']['access_token'], Qparams={
            "page_number": 1,
            "per_page": 1
        })
        self.assertEqual(1, len(response_b.json()['data']['page_records']))

    def test_two_item_per_page(self):
        response_b = OrderApis.order_autocomplete(response_a.json()['data']['access_token'], Qparams={
            "page_number": 1,
            "per_page": 2
        })
        self.assertEqual(2, len(response_b.json()['data']['page_records']))

    def test_two_pages(self):
        response_b = OrderApis.order_autocomplete(response_a.json()['data']['access_token'], Qparams={
            "page_number": 2,
            "per_page": 2
        })
        self.assertEqual(2, len(response_b.json()['data']['page_records']))

    def test_autocomplete_search(self):
        response_b = OrderApis.order_autocomplete(response_a.json()['data']['access_token'], Qparams={
            "page_number": 1,
            "per_page": 2,
            "query": "cak"
        })
        self.assertEqual("cakx1zd", response_b.json()['data']['page_records'][0]['order_id'])

