import random
import string

from API.auth_api import AuthEndPoints
from API.zone_api import ZoneAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiDeleteZone(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        # login
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        # create zone
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

        # delete zone
        global delete_zone_response
        delete_zone_response = ZoneAPI.delete_zone(login_response.json()['data']['access_token'],
                                                   create_zone_response.json()['data']['id'])

    def test_code_status(self):
        self.assertEqual(200, delete_zone_response.status_code)

    def test_confirmation_message(self):
        self.assertEqual("Zone is deleted", delete_zone_response.json()['info']['message'])
