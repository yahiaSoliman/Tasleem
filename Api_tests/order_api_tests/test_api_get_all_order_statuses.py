from API.auth_api import AuthEndPoints
from API.order_api import OrderApis
from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class TestGetAllOrderStatuses(BaseApiClass):

    @classmethod
    def setUpClass(cls):

        response_a = AuthEndPoints.api_login(ApiData.superadmin_username, ApiData.superadmin_password)

        global response_b
        response_b = OrderApis.get_all_order_statuses(response_a.json()['data']['access_token'])

    def test_status_code(self):
        self.assertEqual(200, response_b.status_code)

    def test_first_order_status_id(self):
        self.assertEqual(1, response_b.json()['data'][0]['id'])

    def test_first_order_status_name(self):
        self.assertEqual("preparing", response_b.json()['data'][0]['name'])

    def test_first_order_status_value(self):
        self.assertEqual("Preparing", response_b.json()['data'][0]['value'])

    # -------------------------------------------------------

    def test_second_order_status_id(self):
        self.assertEqual(2, response_b.json()['data'][1]['id'])

    def test_second_order_status_name(self):
        self.assertEqual("ready_for_pick_up", response_b.json()['data'][1]['name'])

    def test_second_order_status_value(self):
        self.assertEqual("Ready For Pick Up", response_b.json()['data'][1]['value'])

    # -------------------------------------------------------

    def test_third_order_status_id(self):
        self.assertEqual(3, response_b.json()['data'][2]['id'])

    def test_third_order_status_name(self):
        self.assertEqual("assigned", response_b.json()['data'][2]['name'])

    def test_third_order_status_value(self):
        self.assertEqual("Assigned", response_b.json()['data'][2]['value'])

    # ---------------------------------------------------------

    def test_fourth_order_status_id(self):
        self.assertEqual(4, response_b.json()['data'][3]['id'])

    def test_fourth_order_status_name(self):
        self.assertEqual("picked_up", response_b.json()['data'][3]['name'])

    def test_fourth_order_status_value(self):
        self.assertEqual("Picked Up", response_b.json()['data'][3]['value'])

    # --------------------------------------------------------

    def test_fifth_order_status_id(self):
        self.assertEqual(5, response_b.json()['data'][4]['id'])

    def test_fifth_order_status_name(self):
        self.assertEqual("on_the_way", response_b.json()['data'][4]['name'])

    def test_fifth_order_status_value(self):
        self.assertEqual("On The Way", response_b.json()['data'][4]['value'])

    # --------------------------------------------------------

    def test_sixth_order_status_id(self):
        self.assertEqual(6, response_b.json()['data'][5]['id'])

    def test_sixth_order_status_name(self):
        self.assertEqual("at_the_address", response_b.json()['data'][5]['name'])

    def test_sixth_order_status_value(self):
        self.assertEqual("At The Address", response_b.json()['data'][5]['value'])

    # -------------------------------------------------------

    def test_seventh_order_status_id(self):
        self.assertEqual(7, response_b.json()['data'][6]['id'])

    def test_seventh_order_status_name(self):
        self.assertEqual("delivered", response_b.json()['data'][6]['name'])

    def test_seventh_order_status_value(self):
        self.assertEqual("Delivered", response_b.json()['data'][6]['value'])

    # -------------------------------------------------------

    def test_eighth_order_status_id(self):
        self.assertEqual(8, response_b.json()['data'][7]['id'])

    def test_eighth_order_status_name(self):
        self.assertEqual("to_return", response_b.json()['data'][7]['name'])

    def test_eighth_order_status_value(self):
        self.assertEqual("To Be Return", response_b.json()['data'][7]['value'])

    # -------------------------------------------------------

    def test_ninth_order_status_id(self):
        self.assertEqual(9, response_b.json()['data'][8]['id'])

    def test_ninth_order_status_name(self):
        self.assertEqual("to_return_assigned", response_b.json()['data'][8]['name'])

    def test_ninth_order_status_value(self):
        self.assertEqual("To Be Return Assigned", response_b.json()['data'][8]['value'])

    # -------------------------------------------------------

    def test_tenth_order_status_id(self):
        self.assertEqual(10, response_b.json()['data'][9]['id'])

    def test_tenth_order_status_name(self):
        self.assertEqual("returned", response_b.json()['data'][9]['name'])

    def test_tenth_order_status_value(self):
        self.assertEqual("Returned", response_b.json()['data'][9]['value'])

    # -------------------------------------------------------

    def test_eleventh_order_status_id(self):
        self.assertEqual(11, response_b.json()['data'][10]['id'])

    def test_eleventh_status_name(self):
        self.assertEqual("delayed", response_b.json()['data'][10]['name'])

    def test_eleventh_order_status_value(self):
        self.assertEqual("Delayed", response_b.json()['data'][10]['value'])

    # ------------------------------------------------------

    def test_twelfth_order_status_id(self):
        self.assertEqual(12, response_b.json()['data'][11]['id'])

    def test_twelfth_status_name(self):
        self.assertEqual("canceled", response_b.json()['data'][11]['name'])

    def test_twelfth_order_status_value(self):
        self.assertEqual("Canceled", response_b.json()['data'][11]['value'])

