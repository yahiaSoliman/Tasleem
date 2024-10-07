from API.auth_api import AuthEndPoints
from core.api_data import ApiData
from core.base_class_api import BaseApiClass
from API.darkstore_api import DarkStoreApis


class GetAllDarkStoresAPI(BaseApiClass):

    @classmethod
    def setUpClass(cls):
        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)
        global response_b
        response_b = DarkStoreApis.api_get_all_darkstore(response_a.json()['data']['access_token'], 1, 1)

    def test_get_all_darkstore_status_code(self):
        self.assertEqual(200, response_b.status_code)

    def test_num_records_type(self):
        self.assertEqual(int, type(response_b.json()['data']['num_records']))

    def test_page_records_type(self):
        self.assertEqual(list, type(response_b.json()['data']['page_records']))

    def test_open_time_type(self):
        self.assertEqual(str, type(response_b.json()['data']['page_records'][0]['open_time']))

    def test_close_time_type(self):
        self.assertEqual(str, type(response_b.json()['data']['page_records'][0]['close_time']))

    def test_longitude_type(self):
        self.assertEqual(float, type(response_b.json()['data']['page_records'][0]['longitude']))

    def test_latitude_type(self):
        self.assertEqual(float, type(response_b.json()['data']['page_records'][0]['latitude']))

    def test_name_type(self):
        self.assertEqual(str, type(response_b.json()['data']['page_records'][0]['name']))

    def test_id_type(self):
        self.assertEqual(int, type(response_b.json()['data']['page_records'][0]['id']))

    def test_city_type(self):
        self.assertEqual(dict, type(response_b.json()['data']['page_records'][0]['city']))

    def test_city_name_type(self):
        self.assertEqual(str, type(response_b.json()['data']['page_records'][0]['city']['name']))

    def test_city_country_name_type(self):
        self.assertEqual(str, type(response_b.json()['data']['page_records'][0]['city']['country_name']))

    def test_city_id_type(self):
        self.assertEqual(int, type(response_b.json()['data']['page_records'][0]['city']['id']))

    # --------------------------------------------------
    # --------------------------------------------------

    def test_waiting_time_type(self):
        self.assertEqual(float, type(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]
                                     ['waiting_time_at_the_darkstore_weight']))

    def test_distance_type(self):
        self.assertEqual(float, type(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]
                                     ['delivered_orders_distance_weight']))

    def test_email_type(self):
        self.assertEqual(str,
                         type(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['email_address']))

    def test_score_divisor_type(self):
        self.assertEqual(dict,
                         type(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['score_divisor']))

    def test_score_divisor_name_type(self):
        self.assertEqual(str, type(
            response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['score_divisor']['name']))

    def test_score_divisor_value_type(self):
        self.assertEqual(int, type(
            response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['score_divisor']['value']))

    def test_stop_auto_assignment_type(self):
        self.assertEqual(bool, type(
            response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['stop_auto_assignment']))

    def test_max_orders_assigned_type(self):
        self.assertEqual(int, type(
            response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['max_orders_assigned']))

    def test_max_interval_time_type(self):
        self.assertEqual(int,
                         type(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['interval_time']))

    def test_delivered_orders_count_weight_type(self):
        self.assertEqual(float,
                         type(response_b.json()['data']['page_records'][0]['darkstore_setting'][0][
                                  'delivered_orders_count_weight']))

    def test_delivered_orders_distance_weight_type(self):
        self.assertEqual(float,
                         type(response_b.json()['data']['page_records'][0]['darkstore_setting'][0][
                                  'delivered_orders_distance_weight']))

    def test_max_threshold_waiting_time_type(self):
        self.assertEqual(int, type(
            response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['max_threshold_waiting_time']))

    def test_interval_weight_type(self):
        self.assertEqual(float,
                         type(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['interval_weight']))
