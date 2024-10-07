from core.selectors import loginPageSelectors


class LoginPage:

    @staticmethod
    def set_username(driver, username_value):
        driver.click(loginPageSelectors.username_input_field)
        driver.clear(loginPageSelectors.username_input_field)
        driver.set_value(loginPageSelectors.username_input_field, username_value)

