from API.auth_api import AuthEndPoints
from API.work_shift_api import WorkShiftApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiWorkShiftTimes(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        # login
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # get shift times
        global shift_times_response
        shift_times_response = WorkShiftApi.get_shifts_time_periods(access_token)

    def test_code_status(self):
        self.assertEqual(200, shift_times_response.status_code)

    def test_id_attribute_type(self):
        self.assertEqual(int, type(shift_times_response.json()['data'][0]['id']))

    def test_start_time_attribute_type(self):
        self.assertEqual(str, type(shift_times_response.json()['data'][0]['shift_start']))

    def test_shift_end(self):
        self.assertEqual(str, type(shift_times_response.json()['data'][0]['shift_end']))

