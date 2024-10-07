import random
import string

from API.auth_api import AuthEndPoints
from API.work_shift_api import WorkShiftApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiGetShift(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        # login
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # create shift
        global shift_name
        shift_name = ''.join(random.choices(string.ascii_lowercase +
                                            string.digits, k=7)) + "automation_test_"

        create_work_shift_response = WorkShiftApi.create_work_shift(access_token, {
            "name":  shift_name,
            "value": "test_value",
            "darkstore_id": 1,
            "shift_start": "15:00:00",
            "shift_end": "23:00:00",
            "description": "test_description"
        })
        global work_shift_id
        get_all_work_shifts_response = WorkShiftApi.get_all_work_shifts(access_token, {"search": shift_name})
        work_shift_id = get_all_work_shifts_response.json()['data']['page_records'][0]['id']

        # get shift
        global get_shift_response
        get_shift_response = WorkShiftApi.get_work_shift(access_token, work_shift_id)

    def test_code_status(self):
        self.assertEqual(200, get_shift_response.status_code)

    def test_shift_description(self):
        self.assertEqual("test_description", get_shift_response.json()['data']['description'])

    def test_shift_start_time(self):
        self.assertEqual("15:00:00", get_shift_response.json()['data']['shift_start'])

    def test_shift_end_time(self):
        self.assertEqual("23:00:00", get_shift_response.json()['data']['shift_end'])

    def test_shift_value(self):
        self.assertEqual("test_value", get_shift_response.json()['data']['value'])

    def test_shift_id(self):
        self.assertEqual(work_shift_id, get_shift_response.json()['data']['id'])

    def test_name(self):
        self.assertEqual(shift_name, get_shift_response.json()['data']['name'])

    def test_darkstore_id(self):
        self.assertEqual(1, get_shift_response.json()['data']['darkstore_id']['id'])

