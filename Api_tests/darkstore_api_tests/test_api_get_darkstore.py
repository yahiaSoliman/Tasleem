from API.auth_api import AuthEndPoints
from API.darkstore_api import DarkStoreApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class GetDarkStoreAPI(BaseApiClass):

    @classmethod
    def setUpClass(cls):

        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        global response_b
        response_b = DarkStoreApis.api_get_all_darkstore(response_a.json()['data']['access_token'], 1, 1)

        global response_c
        response_c = DarkStoreApis.api_get_darkstore(response_a.json()['data']['access_token'],
                                                     response_b.json()['data']['page_records'][0]['id'])

    def test_get_darkstore_status_code(self):
        self.assertEqual(200, response_c.status_code)

    def test_open_time_type(self):
        self.assertEqual(str, type(response_c.json()['data']['open_time']))

    def test_open_time(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['open_time'],
                         response_c.json()['data']['open_time'])

    def test_close_time_type(self):
        self.assertEqual(str, type(response_c.json()['data']['close_time']))

    def test_close_time(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['close_time'],
                         response_c.json()['data']['close_time'])

    def test_longitude_type(self):
        self.assertEqual(float, type(response_c.json()['data']['longitude']))

    def test_longitude(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['longitude'],
                         response_c.json()['data']['longitude'])

    def test_latitude_type(self):
        self.assertEqual(float, type(response_c.json()['data']['latitude']))

    def test_latitude(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['latitude'],
                         response_c.json()['data']['latitude'])

    def test_name_type(self):
        self.assertEqual(str, type(response_c.json()['data']['name']))

    def test_name(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['name'], response_c.json()['data']['name'])

    def test_id_type(self):
        self.assertEqual(int, type(response_c.json()['data']['id']))

    def test_id(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['id'],
                         response_c.json()['data']['id'])

    def test_city_type(self):
        self.assertEqual(dict, type(response_c.json()['data']['city']))

    def test_city_name_type(self):
        self.assertEqual(str, type(response_c.json()['data']['city']['name']))

    def test_city_name(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['city']['name'],
                         response_c.json()['data']['city']['name'])

    def test_city_country_name_type(self):
        self.assertEqual(str, type(response_c.json()['data']['city']['country_name']))

    def test_city_country_name(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['city']['country_name'],
                         response_c.json()['data']['city']['country_name'])

    def test_city_id_type(self):
        self.assertEqual(int, type(response_c.json()['data']['city']['id']))

    def test_city_id(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['city']['id'],
                         response_c.json()['data']['city']['id'])

    # ---------------------------------------------------------
    # ---------------------------------------------------------

    def test_waiting_time_type(self):
        self.assertEqual(float, type(response_c.json()['data']['darkstore_setting'][0]
                                     ['waiting_time_at_the_darkstore_weight']))

    def test_waiting_time(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]
                         ['waiting_time_at_the_darkstore_weight'],
                         response_c.json()['data']['darkstore_setting'][0]
                         ['waiting_time_at_the_darkstore_weight'])

    def test_distance_type(self):
        self.assertEqual(float, type(response_c.json()['data']['darkstore_setting'][0]
                                     ['delivered_orders_distance_weight']))

    def test_distance(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]
                         ['delivered_orders_distance_weight'],
                         response_c.json()['data']['darkstore_setting'][0]
                         ['delivered_orders_distance_weight'])

    def test_email_type(self):
        self.assertEqual(str, type(response_c.json()['data']['darkstore_setting'][0]['email_address']))

    def test_email(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['email_address'],
                         response_c.json()['data']['darkstore_setting'][0]['email_address'])

    def test_score_divisor_type(self):
        self.assertEqual(dict, type(response_c.json()['data']['darkstore_setting'][0]['score_divisor']))

    def test_score_divisor_name_type(self):
        self.assertEqual(str, type(response_c.json()['data']['darkstore_setting'][0]['score_divisor']['name']))

    def test_score_divisor_name(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['score_divisor']['name'],
                         response_c.json()['data']['darkstore_setting'][0]['score_divisor']['name'])

    def test_score_divisor_value_type(self):
        self.assertEqual(int, type(response_c.json()['data']['darkstore_setting'][0]['score_divisor']['value']))

    def test_score_divisor_value(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['score_divisor']['value'],
                         response_c.json()['data']['darkstore_setting'][0]['score_divisor']['value'])

    def test_stop_auto_assignment_type(self):
        self.assertEqual(bool, type(response_c.json()['data']['darkstore_setting'][0]['stop_auto_assignment']))

    def test_stop_auto_assignment(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['stop_auto_assignment'],
                         response_c.json()['data']['darkstore_setting'][0]['stop_auto_assignment'])

    def test_max_orders_assigned_type(self):
        self.assertEqual(int, type(response_c.json()['data']['darkstore_setting'][0]['max_orders_assigned']))

    def test_max_orders_assigned(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['max_orders_assigned'],
                         response_c.json()['data']['darkstore_setting'][0]['max_orders_assigned'])

    def test_max_interval_time_type(self):
        self.assertEqual(int, type(response_c.json()['data']['darkstore_setting'][0]['interval_time']))

    def test_max_interval_time(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['interval_time'],
                         response_c.json()['data']['darkstore_setting'][0]['interval_time'])

    def test_delivered_orders_count_weight_type(self):
        self.assertEqual(float,
                         type(response_c.json()['data']['darkstore_setting'][0]['delivered_orders_count_weight']))

    def test_delivered_orders_count_weight(self):
        self.assertEqual(
            response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['delivered_orders_count_weight'],
            response_c.json()['data']['darkstore_setting'][0]['delivered_orders_count_weight'])

    def test_delivered_orders_distance_weight_type(self):
        self.assertEqual(float,
                         type(response_c.json()['data']['darkstore_setting'][0]['delivered_orders_distance_weight']))

    def test_delivered_orders_distance_weight(self):
        self.assertEqual(
            response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['delivered_orders_distance_weight'],
            response_c.json()['data']['darkstore_setting'][0]['delivered_orders_distance_weight'])

    def test_max_threshold_waiting_time_type(self):
        self.assertEqual(int, type(response_c.json()['data']['darkstore_setting'][0]['max_threshold_waiting_time']))

    def test_max_threshold_waiting_time(self):
        self.assertEqual(
            response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['max_threshold_waiting_time'],
            response_c.json()['data']['darkstore_setting'][0]['max_threshold_waiting_time'])

    def test_interval_weight_type(self):
        self.assertEqual(float, type(response_c.json()['data']['darkstore_setting'][0]['interval_weight']))

    def test_interval_weight(self):
        self.assertEqual(response_b.json()['data']['page_records'][0]['darkstore_setting'][0]['interval_weight'],
                         response_c.json()['data']['darkstore_setting'][0]['interval_weight'])
