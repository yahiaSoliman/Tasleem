import random
import string

from API.auth_api import AuthEndPoints
from API.zone_api import ZoneAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiGetAllZones(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global login_response
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

    def test_code_status(self):
        get_all_zones_response = ZoneAPI.get_all_zones(login_response.json()['data']['access_token'], {})

        self.assertEqual(200, get_all_zones_response.status_code)

    def test_pagination(self):
        get_all_zones_response = ZoneAPI.get_all_zones(login_response.json()['data']['access_token'], {
            "page_number": 1,
            "per_page": 2
        })
        self.assertEqual(2, get_all_zones_response.json()['data']['per_page'])
        self.assertEqual(1, get_all_zones_response.json()['data']['current_page'])
        self.assertEqual(2, len(get_all_zones_response.json()['data']['page_records']))

    def test_item_attribute_types(self):
        get_all_zones_response = ZoneAPI.get_all_zones(login_response.json()['data']['access_token'], {
            "page_number": 1,
            "per_page": 2
        })
        self.assertEqual(str, type(get_all_zones_response.json()['data']['page_records'][0]["name"]))
        self.assertEqual(int, type(get_all_zones_response.json()['data']['page_records'][0]["id"]))
        self.assertEqual(list, type(get_all_zones_response.json()['data']['page_records'][0]["polygon"]))
        self.assertEqual(list, type(get_all_zones_response.json()['data']['page_records'][0]["darkstores"]))

    def test_search(self):
        zone_name = ''.join(random.choices(string.ascii_lowercase +
                                           string.digits, k=7))

        create_zone_response = ZoneAPI.create_zone(login_response.json()['data']['access_token'], payload_dict={
            "name": zone_name,
            "polygon": [
                [
                    33.310204843413416,
                    44.38062824353029
                ],
                [
                    33.30848331776751,
                    44.38135780438234
                ],
                [
                    33.31006138424113,
                    44.38208736523439
                ],
                [
                    33.310168978642494,
                    44.380199090087906
                ]
            ]
        })
        get_all_zones_response = ZoneAPI.get_all_zones(login_response.json()['data']['access_token'], {
            "search": create_zone_response.json()['data']['name']
        })
        self.assertEqual(zone_name, get_all_zones_response.json()['data']['page_records'][0]["name"])






