from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from FEscripts.darkstore_page_selectors import DarkstorePageSelectors


class DarkstorePageInteractions:
    @staticmethod
    def scroll_to_the_target_store(driver, store_name):
        element = driver.find_element(*DarkstorePageSelectors.store_name_selector(store_name))
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    @staticmethod
    def scroll_to_settings_icon(driver, store_name):
        element = driver.find_element(*DarkstorePageSelectors.settings_icon_selector(store_name))
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    @staticmethod
    def click_settings_icon(driver, store_name):
        element = driver.find_element(*DarkstorePageSelectors.settings_icon_selector(store_name))
        element.click()

    @staticmethod
    def scroll_to_auto_assignment(driver):
        element = driver.find_element(*DarkstorePageSelectors.stop_auto_assignment_checkbox_selector)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    @staticmethod
    def click_on_auto_assignment_checkbox(driver):
        element = driver.find_element(*DarkstorePageSelectors.stop_auto_assignment_checkbox_selector)
        element.click()

    @staticmethod
    def scroll_to_save_changes_button(driver):
        element = driver.find_element(*DarkstorePageSelectors.save_changes_button)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    @staticmethod
    def click_save_changes(driver):
        element = driver.find_element(*DarkstorePageSelectors.save_changes_button)
        element.click()

