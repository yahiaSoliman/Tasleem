import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException

from core.mobile_setup import Setup


class BaseClassMob(unittest.TestCase):

    def setUp(self):
        Setup.REMOTE_URL_TUPLE[1].set_capability('name', 'Taza_' + self.__class__.__name__ + ' ' + self._testMethodName)
        self.driver = webdriver.Remote(Setup.REMOTE_URL_TUPLE[0], options=Setup.REMOTE_URL_TUPLE[1], strict_ssl=False)
        self.driver.implicitly_wait(20)

    def find_element(self, selector: tuple):
        return self.driver.find_element(*selector)

    def click(self, element: tuple):
        self.find_element(element).click()

    def set_value(self, selector: tuple, value):
        self.find_element(selector).set_value(value)

    def wait_for_element_visible(self, selector):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(selector))
        except TimeoutException:
            print("element not visible")

    def wait_for_element_not_present(self, selector):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.staleness_of(selector))
        except TimeoutException:
            print("element is still visible")

    def is_displayed(self, element) -> bool:
        try:
            return self.find_element(element).is_displayed()
        except:
            return False

    def press_code(self, key):
        self.driver.press_keycode(key)

    def tap_element_with_relative_coordinate(self, selector, x_coordinate, y_coordinate):
        actions = TouchAction(self.driver)
        e = self.find_element(selector)
        actions.tap(e, x_coordinate, y_coordinate)
        actions.perform()

    def tap_element(self, selector):
        actions = TouchAction(self.driver)
        e = self.find_element(selector)
        actions.tap(e)
        actions.perform()

    def tap_element_with_absolute_coordinates(self, x, y):
        actions = TouchAction(self.driver)
        actions.tap(None, x, y, 1)
        actions.perform()

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def clear(self, selector):
        self.find_element(selector).clear()

    def get_content_desc(self, selector) -> str:
        text = self.find_element(selector).get_attribute('content-desc')
        return text

    def send_keys(self, element: tuple, text: str):
        # self.wait_for_element_visible(element)
        # self.click(element)
        self.find_element(element).send_keys(text)

    def get_text(self, selector):
        element = self.find_element(selector)
        return element.text

    def is_element_displayed(self, selector) -> bool:
        element = self.find_element(selector)
        return element.is_displayed()

    @staticmethod
    def is_device_ios() -> bool:
        if Setup.REMOTE_URL_TUPLE[1].get_capability('platformName').lower() == 'ios':
            return True
        else:
            return False

    def get_number_of_elements(self, selector):
        return len(self.driver.find_elements(*selector))

    def get_list_of_elements(self, selector):
        return self.driver.find_elements(*selector)

    def tearDown(self):
        errors = [error for test, error in self._outcome.errors]
        if any(errors):
            self.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "failure or error"}}')
        self.driver.quit()