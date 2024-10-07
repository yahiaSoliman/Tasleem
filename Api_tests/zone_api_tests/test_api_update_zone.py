import random
import string

from API.auth_api import AuthEndPoints
from API.zone_api import ZoneAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestAPIUpdateZone(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        # login
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        # create zone
        global zone_name
        zone_name = ''.join(random.choices(string.ascii_lowercase +
                                           string.digits, k=7))
        global create_zone_response
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

        # update zone
        global update_zone_response
        update_zone_response = ZoneAPI.update_zone(login_response.json()['data']['access_token'],
                                                   create_zone_response.json()['data']['id'], payload_dict={
                "name": zone_name + 'a',
                "polygon": [
                    [
                        34.310204843413416,
                        45.38062824353029
                    ],
                    [
                        34.30848331776751,
                        45.38135780438234
                    ],
                    [
                        34.31006138424113,
                        45.38208736523439
                    ],
                    [
                        34.310168978642494,
                        45.380199090087906
                    ]
                ]

            })

    def test_code_status(self):
        self.assertEqual(200, update_zone_response.status_code)

    def test_success_message(self):
        self.assertEqual("success", update_zone_response.json()['info']['message'])

    def test_zone_name(self):
        self.assertEqual(zone_name + 'a', update_zone_response.json()['data']['name'])

    def test_zone_id(self):
        self.assertEqual(create_zone_response.json()['data']['id'], update_zone_response.json()['data']['id'])

    def test_polygon_(self):
        self.assertEqual([
            34.310204843413416,
            45.38062824353029
        ], update_zone_response.json()['data']['polygon'][0])

        self.assertEqual([
            34.30848331776751,
            45.38135780438234
        ], update_zone_response.json()['data']['polygon'][1])

        self.assertEqual([
            34.31006138424113,
            45.38208736523439
        ], update_zone_response.json()['data']['polygon'][2])

        self.assertEqual([
            34.310168978642494,
            45.380199090087906
        ], update_zone_response.json()['data']['polygon'][3])
