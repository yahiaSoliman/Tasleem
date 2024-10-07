import time

from FEscripts.base_class import BaseClass
from FEscripts.data_sets import Data
from FEscripts.orders_page_interactions import OrdersPageInteractions


class TestCreateOrder(BaseClass):

    def test_create_order(self):
        self.driver.get("https://admin-ui.dev.tasleem.creativeadvtech.ml")

        OrdersPageInteractions.login(self.driver, Data.super_admin_username, Data.super_admin_password)
        OrdersPageInteractions.click_create_order(self.driver)
        OrdersPageInteractions.insert_order_total(self.driver, Data.order_total)
        OrdersPageInteractions.insert_order_id(self.driver, Data.order_id)
        OrdersPageInteractions.select_store(self.driver, Data.store_name)
        OrdersPageInteractions.select_vehicle(self.driver, Data.vehicle_type)
        OrdersPageInteractions.insert_phone_number(self.driver, Data.phone_number)
        OrdersPageInteractions.select_order_status(self.driver, Data.order_status)
        OrdersPageInteractions.select_merchant(self.driver, Data.merchant_name)
        OrdersPageInteractions.insert_address(self.driver, Data.address)
        OrdersPageInteractions.click_submit(self.driver)

        time.sleep(10)
