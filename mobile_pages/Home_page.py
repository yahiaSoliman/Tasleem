from core.selectors import HomePageSelectors


class HomePage:

    @staticmethod
    def is_home_page_open(driver):
        return driver.is_displayed(HomePageSelectors.is_home_page_open)

    @staticmethod
    def allow_geolocation(driver):
        return driver.click(HomePageSelectors.allow_geolocation)
