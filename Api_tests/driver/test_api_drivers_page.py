from core.api_data import ApiData
from API.auth_api import AuthEndPoints
from core.base_class_api import BaseApiClass
from API.driver_api import DriverEndPoints


class APIDriverDriversPage(BaseApiClass):

    def setUp(self):
        super().setUp()
        global superadmintoken
        global drivers_page_res
        superadmintoken = AuthEndPoints.api_login(self.BASE_URL, ApiData.superadmin_username, ApiData.superadmin_password).json()['data'].get('access_token')
        drivers_page_res = DriverEndPoints.api_drivers_page(self.BASE_URL, superadmintoken)

    # Drivers page response with 200
    # TPI-T452  step 1
    def test_api_drivers_page_statuscode(self):
        self.assertTrue(drivers_page_res.status_code == 200)

    # Drivers page response data is dist
    # TPI-T452  step 2
    def test_api_drivers_page_data(self):
        self.assertTrue(type(drivers_page_res.json()['data']) == dict)

    # Drivers page response data_num_records is int
    # TPI-T452  step 3
    def test_api_drivers_page_data_num_records(self):
        self.assertTrue(type(drivers_page_res.json()['data']['num_records']) == int)

    # Drivers page response data_page_records is list
    # TPI-T452  step 4
    def test_api_drivers_page_data_page_records(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records']) == list)

    # Drivers page response data_per_page is int
    # TPI-T452  step 5
    def test_api_drivers_page_data_per_page(self):
        self.assertTrue(type(drivers_page_res.json()['data']['per_page']) == int)

    # Drivers page response data_current_page is int
    # TPI-T452  step 6
    def test_api_drivers_page_data_current_page(self):
        self.assertTrue(type(drivers_page_res.json()['data']['current_page']) == int)

    # Drivers page response data_num_pages is int
    # TPI-T452  step 7
    def test_api_drivers_page_data_num_pages(self):
        self.assertTrue(type(drivers_page_res.json()['data']['num_pages']) == int)

    # Drivers page response data_page_records_id is int
    # TPI-T452  step 8
    def test_api_drivers_page_data_page_records_id(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['id']) == int)

    # Drivers page response data_page_records_is_clock_in is bool
    # TPI-T452  step 9
    def test_api_drivers_page_data_page_records_is_clock_in(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['is_clock_in']) == bool)

    # Drivers page response data_page_records_is_busy is int
    # TPI-T452  step 10
    def test_api_drivers_page_data_page_records_is_busy(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['is_busy']) == int)

    # Drivers page response data_page_records_license is str
    # TPI-T452  step 11
    def test_api_drivers_page_data_page_records_license(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['license']) == str)

    # Drivers page response data_page_records_box_number is str
    # TPI-T452  step 12
    def test_api_drivers_page_data_page_records_box_number(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['box_number']) == str)

    # Drivers page response data_page_records_driver_license_no is str
    # TPI-T452  step 13
    def test_api_drivers_page_data_page_records_driver_license_no(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_license_no']) == str)

    # Drivers page response data_page_records_created_at is str
    # TPI-T452  step 14
    def test_api_drivers_page_data_page_records_created_at(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['created_at']) == str)

    # Drivers page response data_page_records_darkstore is dict
    # TPI-T452  step 15
    def test_api_drivers_page_data_page_records_darkstore(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['darkstore']) == dict)

    # Drivers page response data_page_records_driver_address is dict
    # TPI-T452  step 16
    def test_api_drivers_page_data_page_records_driver_address(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_address']) == dict)

    # Drivers page response data_page_records_vehicle_id is dict
    # TPI-T452  step 17
    def test_api_drivers_page_data_page_records_vehicle_id(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']) == dict)

    # Drivers page response data_page_records_last_location is dict
    # TPI-T452  step 18
    def test_api_drivers_page_data_page_records_last_location(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['last_location']) == dict)

    # Drivers page response data_page_records_driver_info is dict
    # TPI-T452  step 19
    def test_api_drivers_page_data_page_records_driver_info(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_info']) == dict)

    # Drivers page response data_page_records_shift is dict
    # TPI-T452  step 20
    def test_api_drivers_page_data_page_records_shift(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['shift']) == dict)

    # Drivers page response data_page_records_driver_status is dict
    # TPI-T452  step 21
    def test_api_drivers_page_data_page_records_driver_status(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_status']) == dict)

    # Drivers page response data_page_records_city is dict
    # TPI-T452  step 22
    def test_api_drivers_page_data_page_records_city(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['city']) == dict)

    # Drivers page response data_page_records_darkstore_longitude is float
    # TPI-T452  step 23
    def test_api_drivers_page_data_page_records_darkstore_longitude(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['darkstore']['longitude']) == float)

    # Drivers page response data_page_records_darkstore_latitude is float
    # TPI-T452  step 24
    def test_api_drivers_page_data_page_records_darkstore_latitude(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['darkstore']['latitude']) == float)

    # Drivers page response data_page_records_darkstore_id is int
    # TPI-T452  step 25
    def test_api_drivers_page_data_page_records_darkstore_id(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['darkstore']['id']) == int)

    # Drivers page response data_page_records_darkstore_darkstore_setting is dict
    # TPI-T452  step 26
    def test_api_drivers_page_data_page_records_darkstore_darkstore_setting(self):
        self.assertTrue(
            type(drivers_page_res.json()['data']['page_records'][0]['darkstore']['darkstore_setting']) == list)

    # Drivers page response data_page_records_darkstore_darkstore_setting_max_distance_from_dark_store is int
    # TPI-T452  step 27
    def test_api_drivers_page_data_page_records_darkstore_darkstore_setting_max_distance_from_dark_store(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['darkstore']['darkstore_setting'][0][
                                 'max_distance_from_dark_store']) == int)

    # Drivers page response data_page_records_driver_address_address_building is str
    # TPI-T452  step 28
    def test_api_drivers_page_data_page_records_driver_address_address_building(self):
        self.assertTrue(
            type(drivers_page_res.json()['data']['page_records'][0]['driver_address']['address_building']) == str)

    # Drivers page response data_page_records_driver_address_address_district is str
    # TPI-T452  step 29
    def test_api_drivers_page_data_page_records_driver_address_address_district(self):
        self.assertTrue(
            type(drivers_page_res.json()['data']['page_records'][0]['driver_address']['address_district']) == str)

    # Drivers page response data_page_records_driver_address_address_flat is str
    # TPI-T452  step 30
    def test_api_drivers_page_data_page_records_driver_address_address_flat(self):
        self.assertTrue(
            type(drivers_page_res.json()['data']['page_records'][0]['driver_address']['address_flat']) == str)

    # Drivers page response data_page_records_driver_address_address_floor is str
    # TPI-T452  step 31
    def test_api_drivers_page_data_page_records_driver_address_address_floor(self):
        self.assertTrue(
            type(drivers_page_res.json()['data']['page_records'][0]['driver_address']['address_floor']) == str)

    # Drivers page response data_page_records_driver_address_address_nearest_landmark is str
    # TPI-T452  step 32
    def test_api_drivers_page_data_page_records_driver_address_address_nearest_landmark(self):
        self.assertTrue(type(
            drivers_page_res.json()['data']['page_records'][0]['driver_address']['address_nearest_landmark']) == str)

    # Drivers page response data_page_records_driver_address_address_neighborhood is str
    # TPI-T452  step 33
    def test_api_drivers_page_data_page_records_driver_address_address_neighborhood(self):
        self.assertTrue(
            type(drivers_page_res.json()['data']['page_records'][0]['driver_address']['address_neighborhood']) == str)

    # Drivers page response data_page_records_vehicle_id_is_assigned is bool
    # TPI-T452  step 34
    def test_api_drivers_page_data_page_records_vehicle_id_is_assigned(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['is_assigned']) == bool)

    # Drivers page response data_page_records_vehicle_id_is_activated is bool
    # TPI-T452  step 35
    def test_api_drivers_page_data_page_records_vehicle_id_is_activated(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['is_activated']) == bool)

    # Drivers page response data_page_records_vehicle_id_id is int
    # TPI-T452  step 36
    def test_api_drivers_page_data_page_records_vehicle_id_id(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['id']) == int)

    # Drivers page response data_page_records_vehicle_id_make is str
    # TPI-T452  step 37
    def test_api_drivers_page_data_page_records_vehicle_id_make(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['make']) == str)

    # Drivers page response data_page_records_vehicle_id_license_no is str
    # TPI-T452  step 38
    def test_api_drivers_page_data_page_records_vehicle_id_license_no(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['license_no']) == str)

    # Drivers page response data_page_records_vehicle_id_owner is str
    # TPI-T452  step 39
    def test_api_drivers_page_data_page_records_vehicle_id_owner(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['owner']) == str)

    # Drivers page response data_page_records_vehicle_id_year is str
    # TPI-T452  step 40
    def test_api_drivers_page_data_page_records_vehicle_id_year(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['year']) == str)

    # Drivers page response data_page_records_vehicle_id_model is str
    # TPI-T452  step 41
    def test_api_drivers_page_data_page_records_vehicle_id_model(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['model']) == str)

    # Drivers page response data_page_records_vehicle_id_is_assigned is str
    # TPI-T452  step 42
    def test_api_drivers_page_data_page_records_vehicle_id_name(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['name']) == str)

    # Drivers page response data_page_records_vehicle_id_vehicle_type is dict
    # TPI-T452  step 43
    def test_api_drivers_page_data_page_records_vehicle_id_vehicle_type(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['vehicle_type']) == dict)

    # Drivers page response data_page_records_vehicle_id_vehicle_type_value is str
    # TPI-T452  step 44
    def test_api_drivers_page_data_page_records_vehicle_id_vehicle_type_value(self):
        self.assertTrue(
            type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['vehicle_type']['value']) == str)

    # Drivers page response data_page_records_vehicle_id_vehicle_type_id is int
    # TPI-T452  step 45
    def test_api_drivers_page_data_page_records_vehicle_id_vehicle_type_id(self):
        self.assertTrue(
            type(drivers_page_res.json()['data']['page_records'][0]['vehicle_id']['vehicle_type']['id']) == int)

    # Drivers page response data_page_records_last_location_latitude is float or int
    # TPI-T452  step 46
    def test_api_drivers_page_data_page_records_last_location_latitude(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['last_location']['latitude']) == float or int)

    # Drivers page response data_page_records_last_location_longitude is float or int
    # TPI-T452  step 47
    def test_api_drivers_page_data_page_records_last_location_longitude(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['last_location']['longitude']) == float or int)

    # Drivers page response data_page_records_driver_info_id is int
    # TPI-T452  step 48
    def test_api_drivers_page_data_page_records_driver_info_id(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_info']['id']) == int)

    # Drivers page response data_page_records_driver_info_last_name is str
    # TPI-T452  step 49
    def test_api_drivers_page_data_page_records_driver_info_last_name(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_info']['last_name']) == str)

    # Drivers page response data_page_records_driver_info_first_name is str
    # TPI-T452  step 50
    def test_api_drivers_page_data_page_records_driver_info_first_name(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_info']['first_name']) == str)

    # Drivers page response data_page_records_driver_info_username is str
    # TPI-T452  step 51
    def test_api_drivers_page_data_page_records_driver_info_username(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_info']['username']) == str)

    # Drivers page response data_page_records_driver_info_user_phone_number is str
    # TPI-T452  step 52
    def test_api_drivers_page_data_page_records_driver_info_user_phone_number(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_info']['user_phone_number']) == str)

    # Drivers page response data_page_records_shift_id is int
    # TPI-T452  step 53
    def test_api_drivers_page_data_page_records_shift_id(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['shift']['id']) == int)

    # Drivers page response data_page_records_shift_shift_start is str
    # TPI-T452  step 54
    def test_api_drivers_page_data_page_records_shift_shift_start(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['shift']['shift_start']) == str)

    # Drivers page response data_page_records_shift_shift_end is str
    # TPI-T452  step 55
    def test_api_drivers_page_data_page_records_shift_shift_end(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['shift']['shift_end']) == str)

    # Drivers page response data_page_records_driver_status_id is int
    # TPI-T452  step 56
    def test_api_drivers_page_data_page_records_driver_status_id(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_status']['id']) == int)

    # Drivers page response data_page_records_driver_status_name is str
    # TPI-T452  step 57
    def test_api_drivers_page_data_page_records_driver_status_name(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_status']['name']) == str)

    # Drivers page response data_page_records_driver_status_value is str
    # TPI-T452  step 58
    def test_api_drivers_page_data_page_records_driver_status_value(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['driver_status']['value']) == str)

    # Drivers page response data_page_records_city_id is int
    # TPI-T452  step 59
    def test_api_drivers_page_data_page_records_city_id(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['city']['id']) == int)

    # Drivers page response data_page_records_city_country_name is str
    # TPI-T452  step 60
    def test_api_drivers_page_data_page_records_city_country_name(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['city']['country_name']) == str)

    # Drivers page response data_page_records_city_name is str
    # TPI-T452  step 61
    def test_api_drivers_page_data_page_records_city_name(self):
        self.assertTrue(type(drivers_page_res.json()['data']['page_records'][0]['city']['name']) == str)





















