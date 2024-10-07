import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from FEscripts.base_class import BaseClass
from FEscripts.darkstore_page_interactions import DarkstorePageInteractions
from FEscripts.data_sets import Data
from FEscripts.orders_page_interactions import OrdersPageInteractions


class TestStoreSettings(BaseClass):

    def test_update_settings(self):
        self.driver.get("https://admin-ui.dev.tasleem.creativeadvtech.ml")
        OrdersPageInteractions.login(self.driver, Data.super_admin_username, Data.super_admin_password)
        self.driver.get("https://admin-ui.dev.tasleem.creativeadvtech.ml/#/dark-stores")

        DarkstorePageInteractions.scroll_to_the_target_store(self.driver, Data.store_name_to_update_settings)
        DarkstorePageInteractions.scroll_to_settings_icon(self.driver, Data.store_name_to_update_settings)
        DarkstorePageInteractions.click_settings_icon(self.driver, Data.store_name_to_update_settings)
        time.sleep(2)
        DarkstorePageInteractions.scroll_to_auto_assignment(self.driver)
        DarkstorePageInteractions.click_on_auto_assignment_checkbox(self.driver)
        DarkstorePageInteractions.scroll_to_save_changes_button(self.driver)
        time.sleep(2)
        DarkstorePageInteractions.click_save_changes(self.driver)
        time.sleep(10)
