import random
import string

from API.auth_api import AuthEndPoints
from API.zone_api import ZoneAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiAssignZone(BaseApiClass):

    @classmethod
    def setUpClass(cls):

        # login and get access token
        global access_token
        access_token = cls.get_access_token()

        # create zone and get its id
        global zone_id
        zone_id = cls.get_zone_id()

        # assign zone to darkstore
        global assign_zone_response
        darkstore_id = 1
        assign_zone_response = ZoneAPI.assign_darkstore_to_zone(access_token, darkstore_id, zone_id)

    def test_code_status(self):
        self.assertEqual(200, assign_zone_response.status_code)

    def test_confirmation_message(self):
        self.assertEqual(
            "Zone " + str(zone_id) + " is assigned to darkstore successfully",
            assign_zone_response.json()['info']['message'])

    def test_darkstore_in_get_zone_response(self):
        get_zone_response = ZoneAPI.get_zone(access_token, zone_id)
        self.assertEqual(1, len(get_zone_response.json()['data']['darkstores']))
        self.assertEqual(1, get_zone_response.json()['data']['darkstores'][0]['id'])

    # --------------------------------------------------------------
    # --------------------------------------------------------------

    @staticmethod
    def get_zone_id():
        zone_name = ''.join(random.choices(string.ascii_lowercase +
                                           string.digits, k=7))

        response = ZoneAPI.create_zone(access_token, payload_dict={
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
        return response.json()['data']['id']

    @classmethod
    def get_access_token(cls):
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        return login_response.json()['data']['access_token']
