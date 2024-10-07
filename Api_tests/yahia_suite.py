import unittest

from Api_tests.darkstore_api_tests.test_api_get_darkstore import GetDarkStoreAPI
from Api_tests.darkstore_api_tests.test_api_update_store_settings import UpdateStoreSettingsAPI
from Api_tests.darkstore_api_tests.test_get_all_darkstores import GetAllDarkStoresAPI
from Api_tests.order_api_tests.tes_api_create_order import TestCreateOrderApi
from Api_tests.order_api_tests.test_api_cancel_order import TestCancelOrderApi
from Api_tests.order_api_tests.test_api_get_all_order_statuses import TestGetAllOrderStatuses
from Api_tests.order_api_tests.test_api_get_all_orders import TestGelAllOrdersApi
from Api_tests.order_api_tests.test_api_get_order import TestGetOrderApi
from Api_tests.order_api_tests.test_api_get_order_detail import TestApiOrderDetails
from Api_tests.order_api_tests.test_api_get_order_latest_statuses import TestGetOrderLatestStatuses
from Api_tests.order_api_tests.test_api_set_order_status_ready_for_pickup import TestSetOrderStatusReadyForPickupApi
from Api_tests.user_api_tests.tes_api_get_roles import TestApiGetRoles
from Api_tests.user_api_tests.test_api_change_user_password import TestApiChangePassword
from Api_tests.user_api_tests.test_api_deactivate_user import TestApiDeactivateUser
from Api_tests.user_api_tests.test_api_get_user_data import TestApiGetUserData
from Api_tests.user_api_tests.test_api_invite_check import TestApiInviteCheck
from Api_tests.user_api_tests.test_api_invite_user import TestApiInviteUser
from Api_tests.user_api_tests.test_api_update_user_data import TestApiUpdateUserData
from Api_tests.vehicles_api_tests.test_api_activate_vehicle import TestApiActivateVehicle
from Api_tests.vehicles_api_tests.test_api_create_vehicle import TestApiCreateVehicle
from Api_tests.vehicles_api_tests.test_api_delete_vehicle import TestApiDeleteVehicle
from Api_tests.vehicles_api_tests.test_api_get_all_vehicle_types import TestApiGetAllVehicleTypes
from Api_tests.vehicles_api_tests.test_api_get_vehicle import TestApiGetVehicle
from Api_tests.vehicles_api_tests.test_api_update_vehicle import TestApiUpdateVehicle
from Api_tests.work_shift_api_tests.test_api_delete_work_shift import TestApiDeleteWorkShift
from Api_tests.work_shift_api_tests.test_api_get_all_work_shifts import TestApiGetAllWorkShifts
from Api_tests.work_shift_api_tests.test_api_get_shift import TestApiGetShift
from Api_tests.work_shift_api_tests.test_api_get_shift_times import TestApiWorkShiftTimes
from Api_tests.work_shift_api_tests.test_api_update_work_shift import TestApiUpdateWorkShift
from Api_tests.work_shift_api_tests.test_create_work_shift import TestApiCreateWorkShift
from Api_tests.zone_api_tests.test_api_assign_darkstore_zone import TestApiAssignZone
from Api_tests.zone_api_tests.test_api_create_zone import TestAPICreateZone
from Api_tests.zone_api_tests.test_api_delete_zone import TestApiDeleteZone
from Api_tests.zone_api_tests.test_api_get_all_zones import TestApiGetAllZones
from Api_tests.zone_api_tests.test_api_get_zone import TestAPIGetZone
from Api_tests.zone_api_tests.test_api_unassign_darkstore_zone import TestApiUnassignZone
from Api_tests.zone_api_tests.test_api_update_zone import TestAPIUpdateZone


def suite_of_vehicle():
    vehicle_suite = unittest.TestSuite()
    vehicle_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiActivateVehicle))
    vehicle_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiCreateVehicle))
    vehicle_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiDeleteVehicle))
    vehicle_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiGetAllVehicleTypes))
    vehicle_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiGetVehicle))
    vehicle_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiUpdateVehicle))

    return vehicle_suite


def suite_of_zone():
    zone_suite = unittest.TestSuite()
    zone_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiGetAllZones))
    zone_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAPIGetZone))
    zone_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAPICreateZone))
    zone_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAPIUpdateZone))
    zone_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiDeleteZone))
    zone_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiAssignZone))
    zone_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiUnassignZone))

    return zone_suite


def suite_of_darkstore():
    darkstore_suite = unittest.TestSuite()
    darkstore_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(GetAllDarkStoresAPI))
    darkstore_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(GetDarkStoreAPI))
    darkstore_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UpdateStoreSettingsAPI))

    return darkstore_suite


def suite_of_order():
    order_suite = unittest.TestSuite()
    order_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCreateOrderApi))
    order_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCancelOrderApi))
    order_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGetAllOrderStatuses))
    order_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGelAllOrdersApi))
    order_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGetOrderApi))
    order_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiOrderDetails))
    order_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGetOrderLatestStatuses))
    order_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSetOrderStatusReadyForPickupApi))

    return order_suite


def suite_of_work_shift():
    work_shift_suite = unittest.TestSuite()
    work_shift_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiDeleteWorkShift))
    work_shift_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiGetAllWorkShifts))
    work_shift_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiGetShift))
    work_shift_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiUpdateWorkShift))
    work_shift_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiCreateWorkShift))
    work_shift_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiWorkShiftTimes))

    return work_shift_suite


def suite_of_user():
    user_suite = unittest.TestSuite()
    user_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiGetRoles))
    user_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiInviteCheck))
    user_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiInviteUser))
    user_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiChangePassword))
    user_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiDeactivateUser))
    user_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiGetUserData))
    user_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApiUpdateUserData))

    return user_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    runner.run(suite_of_vehicle())
    print("end of 1st suite")

    y = runner.run(suite_of_zone())
    print("end of 2nd suite")

    runner.run(suite_of_darkstore())
    print("end of 3rd suite")

    runner.run(suite_of_order())
    print("end of 4th suite")

    runner.run(suite_of_work_shift())
    print("end of 5th suite")

    runner.run(suite_of_user())
    print("end of 6th suite")