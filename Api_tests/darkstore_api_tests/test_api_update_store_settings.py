from API.auth_api import AuthEndPoints
from API.darkstore_api import DarkStoreApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class UpdateStoreSettingsAPI(BaseApiClass):
    @classmethod
    def setUpClass(cls):
        # login
        global access_token
        login_response = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        access_token = login_response.json()['data']['access_token']

        # update settings
        global update_store_response
        update_store_response = DarkStoreApis.api_update_store_settings(access_token, "1", {
            "max_threshold_waiting_time": 20,
            "max_orders_assigned": 2,
            "email_address": "update-store@gmail.com",
            "max_distance_from_dark_store": 200,
            "score_divisor": 2,
            "interval_time": 90,
            "interval_weight": 2,
            "stop_auto_assignment": True,
            "stop_auto_clock_out": True,
            "delivered_orders_count_weight": 0.4,
            "delivered_orders_distance_weight": 0.3,
            "waiting_time_at_the_darkstore_weight": 0.3
        })

        # get store data after first update
        global get_darkstore_response
        get_darkstore_response = DarkStoreApis.api_get_darkstore(access_token, "1")

        # update settings for the second time
        global second_update_store_response
        second_update_store_response = DarkStoreApis.api_update_store_settings(access_token, "1", {
            "max_threshold_waiting_time": 60,
            "max_orders_assigned": 3,
            "email_address": "dark-store@gmail.com",
            "max_distance_from_dark_store": 100,
            "score_divisor": 1,
            "interval_time": 60,
            "interval_weight": 1,
            "stop_auto_assignment": False,
            "stop_auto_clock_out": False,
            "delivered_orders_count_weight": 0.2,
            "delivered_orders_distance_weight": 0.2,
            "waiting_time_at_the_darkstore_weight": 0.6
        })

        # get store data after second update
        global get_darkstore_response_after_second_update
        get_darkstore_response_after_second_update = DarkStoreApis.api_get_darkstore(access_token, "1")

    def test_code_status_first_call(self):
        self.assertEqual(200, update_store_response.status_code)

    def test_stop_auto_assignment_after_first_update(self):
        self.assertEqual(True, get_darkstore_response.json()['data']['darkstore_setting'][0]['stop_auto_assignment'])

    def test_stop_auto_clock_out_after_first_update(self):
        self.assertEqual(True, get_darkstore_response.json()['data']['darkstore_setting'][0]['stop_auto_clock_out'])

    def test_max_threshold_waiting_time_after_first_update(self):
        self.assertEqual(20, get_darkstore_response.json()['data']['darkstore_setting'][0]['max_threshold_waiting_time'])

    def test_max_orders_assigned_after_first_update(self):
        self.assertEqual(2, get_darkstore_response.json()['data']['darkstore_setting'][0]['max_orders_assigned'])

    def test_email_address_after_first_update(self):
        self.assertEqual("update-store@gmail.com", get_darkstore_response.json()['data']['darkstore_setting'][0]['email_address'])

    def test_max_distance_from_dark_store_after_first_update(self):
        self.assertEqual(200, get_darkstore_response.json()['data']['darkstore_setting'][0]['max_distance_from_dark_store'])

    def test_score_divisor_after_first_update(self):
        self.assertEqual(2, get_darkstore_response.json()['data']['darkstore_setting'][0]['score_divisor']['value'])

    def test_interval_time_after_first_update(self):
        self.assertEqual(90, get_darkstore_response.json()['data']['darkstore_setting'][0]['interval_time'])

    def test_interval_weight_after_first_update(self):
        self.assertEqual(2, get_darkstore_response.json()['data']['darkstore_setting'][0]['interval_weight'])

    def test_delivered_orders_count_weight_after_first_update(self):
        self.assertEqual(0.4, get_darkstore_response.json()['data']['darkstore_setting'][0]['delivered_orders_count_weight'])

    def test_delivered_orders_distance_weight_after_first_update(self):
        self.assertEqual(0.3, get_darkstore_response.json()['data']['darkstore_setting'][0]['delivered_orders_distance_weight'])

    def test_waiting_time_at_the_darkstore_weight_after_first_update(self):
        self.assertEqual(0.3, get_darkstore_response.json()['data']['darkstore_setting'][0]['waiting_time_at_the_darkstore_weight'])

        # --------------------------------------------------------------------------
        # --------------------------------------------------------------------------

    def test_code_status_second_call(self):
        self.assertEqual(200, second_update_store_response.status_code)

    def test_stop_auto_assignment_after_second_update(self):
        self.assertEqual(False, get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['stop_auto_assignment'])

    def test_stop_auto_clock_out_after_second_update(self):
        self.assertEqual(False, get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['stop_auto_clock_out'])

    def test_max_threshold_waiting_time_after_second_update(self):
        self.assertEqual(60,
                         get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['max_threshold_waiting_time'])

    def test_max_orders_assigned_after_second_update(self):
        self.assertEqual(3, get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['max_orders_assigned'])

    def test_email_address_after_second_update(self):
        self.assertEqual("dark-store@gmail.com",
                         get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['email_address'])

    def test_max_distance_from_dark_store_after_second_update(self):
        self.assertEqual(100,
                         get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['max_distance_from_dark_store'])

    def test_score_divisor_after_second_update(self):
        self.assertEqual(1, get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['score_divisor']['value'])

    def test_interval_time_after_second_update(self):
        self.assertEqual(60, get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['interval_time'])

    def test_interval_weight_after_second_update(self):
        self.assertEqual(1, get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['interval_weight'])

    def test_delivered_orders_count_weight_after_second_update(self):
        self.assertEqual(0.2,
                         get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0]['delivered_orders_count_weight'])

    def test_delivered_orders_distance_weight_after_second_update(self):
        self.assertEqual(0.2, get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0][
            'delivered_orders_distance_weight'])

    def test_waiting_time_at_the_darkstore_weight_after_second_update(self):
        self.assertEqual(0.6, get_darkstore_response_after_second_update.json()['data']['darkstore_setting'][0][
            'waiting_time_at_the_darkstore_weight'])

