import base64
import time

from FEscripts.base_class import BaseClass
from selenium.webdriver.common.by import By


class LocateByImage(BaseClass):

    def test_create_order_button_image(self):
        self.driver.get("https://admin-ui.dev.tasleem.creativeadvtech.ml")
        image_string = open("create_order.jpg", "rb")
        encoded_image = base64.b64encode(image_string.read())
        e = self.driver.find_element(By.)
        time.sleep(5)
