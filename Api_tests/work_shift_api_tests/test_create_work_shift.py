import random
import string

from API.auth_api import AuthEndPoints
from API.work_shift_api import WorkShiftApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiCreateWorkShift(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        # login
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # create work shift
        global shift_name
        shift_name = ''.join(random.choices(string.ascii_lowercase +
                                            string.digits, k=7))

        global create_work_shift_response
        create_work_shift_response = WorkShiftApi.create_work_shift(access_token, {
            "name": "automation_test_" + shift_name,
            "value": "test_value",
            "darkstore_id": 1,
            "shift_start": "15:00:00",
            "shift_end": "23:00:00",
            "description": "test_description"
        })

    def test_code_status(self):
        self.assertEqual(200, create_work_shift_response.status_code)

    def test_confirmation_message(self):
        self.assertEqual("Shift created successfully", create_work_shift_response.json()['info']['message'])
