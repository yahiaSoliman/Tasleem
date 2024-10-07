import random
import string

from API.auth_api import AuthEndPoints
from API.work_shift_api import WorkShiftApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiDeleteWorkShift(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        global access_token
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # create shift
        shift_name = ''.join(random.choices(string.ascii_lowercase +
                                            string.digits, k=7))

        create_work_shift_response = WorkShiftApi.create_work_shift(access_token, {
            "name": "automation_test_" + shift_name,
            "value": "test_value",
            "darkstore_id": 1,
            "shift_start": "15:00:00",
            "shift_end": "23:00:00",
            "description": "test_description"
        })
        global work_shift_id
        get_all_work_shifts_response = WorkShiftApi.get_all_work_shifts(access_token, {"search": shift_name})
        work_shift_id = get_all_work_shifts_response.json()['data']['page_records'][0]['id']

        # delete work shift
        global delete_shift_response
        delete_shift_response = WorkShiftApi.delete_work_shift(access_token, work_shift_id)

    def test_code_status(self):
        self.assertEqual(200, delete_shift_response.status_code)

    def test_confirmation_message(self):
        self.assertEqual("Shift with id: " + str(work_shift_id) + " deleted successfully.", delete_shift_response.json()['info']['message'])

