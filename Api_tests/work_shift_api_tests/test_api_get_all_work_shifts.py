from API.auth_api import AuthEndPoints
from API.work_shift_api import WorkShiftApi
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestApiGetAllWorkShifts(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        # login
        global access_token
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # get all work shifts
        global get_all_work_shifts_response
        get_all_work_shifts_response = WorkShiftApi.get_all_work_shifts(access_token, {
            "page_number": 1,
            "per_page": 2
        })

    def test_pagination(self):
        self.assertEqual(2, get_all_work_shifts_response.json()['data']['per_page'])
        self.assertEqual(1, get_all_work_shifts_response.json()['data']['current_page'])
        self.assertEqual(2, len(get_all_work_shifts_response.json()['data']['page_records']))

    def test_type_of_attribute_description(self):
        self.assertEqual(str, type(get_all_work_shifts_response.json()['data']['page_records'][0]['description']))

    def test_type_of_attribute_name(self):
        self.assertEqual(str, type(get_all_work_shifts_response.json()['data']['page_records'][0]['name']))

    def test_type_of_attribute_id(self):
        self.assertEqual(int, type(get_all_work_shifts_response.json()['data']['page_records'][0]['id']))

    def test_type_of_attribute_shift_start(self):
        self.assertEqual(str, type(get_all_work_shifts_response.json()['data']['page_records'][0]['shift_start']))

    def test_type_of_attribute_shift_end(self):
        self.assertEqual(str, type(get_all_work_shifts_response.json()['data']['page_records'][0]['shift_end']))

    def test_type_of_attribute_value(self):
        self.assertEqual(str, type(get_all_work_shifts_response.json()['data']['page_records'][0]['value']))

    def test_type_of_attribute_darkstore_id(self):
        self.assertEqual(dict, type(get_all_work_shifts_response.json()['data']['page_records'][0]['darkstore_id']))

    def test_search(self):
        search_query = get_all_work_shifts_response.json()['data']['page_records'][1]['name']
        response = WorkShiftApi.get_all_work_shifts(access_token, {"search": search_query})
        for x in response.json()['data']['page_records']:
            self.assertEqual(search_query, x['name'])




