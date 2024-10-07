from core.base_class_web import BaseClassWeb


class WebLoginTest(BaseClassWeb):

    def test_login(self):
        self.driver.get("https://admin-ui.dev.tasleem.creativeadvtech.m")
        print(self.driver.title)
        self.tearDown()



