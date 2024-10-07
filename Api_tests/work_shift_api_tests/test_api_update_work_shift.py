import random
import string

from API.auth_api import AuthEndPoints
from API.work_shift_api import WorkShiftApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiUpdateWorkShift(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        # login
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # create work shift
        shift_name = "automation_test_" + ''.join(random.choices(string.ascii_lowercase +
                                                                 string.digits, k=7))

        WorkShiftApi.create_work_shift(access_token, {
            "name": shift_name,
            "value": "test_value",
            "darkstore_id": 1,
            "shift_start": "15:00:00",
            "shift_end": "23:00:00",
            "description": "test_description"
        })

        # get work shift id
        response = WorkShiftApi.get_all_work_shifts(access_token, {"search": shift_name})
        global  work_shift_id
        work_shift_id = response.json()['data']['page_records'][0]['id']

        # update work shift
        shift_name = "updated_automation_test_" + ''.join(random.choices(string.ascii_lowercase +
                                                                         string.digits, k=7))
        global response_of_update_shift
        response_of_update_shift = WorkShiftApi.update_work_shift(access_token, {
            "name": shift_name,
            "value": "test_value",
            "darkstore_id": 1,
            "shift_start": "15:00:00",
            "shift_end": "23:00:00",
            "description": "test_description"
        }, work_shift_id)

    def test_code_status(self):
        self.assertEqual(200, response_of_update_shift.status_code)

    def test_confirmation_message(self):
        self.assertEqual("Shift with id: " + str(work_shift_id) + " updated successfully", response_of_update_shift.json()['info']['message'])
