from core.base_class_mob import BaseClassMob
from core.data_sets import DataSets
from mobile_pages.login_page import LoginPage
from mobile_pages.Home_page import HomePage


class LoginTest(BaseClassMob):

    def test_login(self):
        LoginPage.login(self, DataSets.driver_username, DataSets.driver_password)
        HomePage.allow_geolocation(self)
        result = HomePage.is_home_page_open(self)
        self.assertTrue(result)



