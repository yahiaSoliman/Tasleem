import random
import string
import unittest

from API.auth_api import AuthEndPoints
from API.zone_api import ZoneAPI
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiUnassignZone(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login as super admin and get access token
        global access_token
        access_token = cls.get_access_token()

        # create new zone and get its ID
        global zone_id
        zone_id = cls.get_zone_id()

        # assign zone to darkstore
        darkstore_id = 1
        ZoneAPI.assign_darkstore_to_zone(access_token, darkstore_id, zone_id)

        # unassign zone to darkstore
        global unassign_zone_response
        unassign_zone_response = ZoneAPI.unassign_darkstore_to_zone(access_token, darkstore_id, zone_id)

    def test_code_status(self):
        self.assertEqual(200, unassign_zone_response.status_code)

    def test_confirmation_message(self):
        self.assertEqual("Zone " + str(zone_id) + " is unassigned from darkstore successfully",
                         unassign_zone_response.json()['info']['message'])

    def test_darkstore_in_get_zone_response(self):
        get_zone_response = ZoneAPI.get_zone(access_token, zone_id)
        self.assertEqual(0, len(get_zone_response.json()['data']['darkstores']))

    # ---------------------------------------------------------
    # ---------------------------------------------------------
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
