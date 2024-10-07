from core.selectors import loginPageSelectors


class LoginPage:

    @staticmethod
    def set_username(driver, username_value):
        driver.click(loginPageSelectors.username_input_field)
        driver.clear(loginPageSelectors.username_input_field)
        driver.set_value(loginPageSelectors.username_input_field, username_value)

    @staticmethod
    def set_password(driver, password_value):
        driver.click(loginPageSelectors.password_input_field)
        driver.clear(loginPageSelectors.password_input_field)
        driver.set_value(loginPageSelectors.password_input_field, password_value)

    @staticmethod
    def click_log_in_button(driver):
        driver.click(loginPageSelectors.loginButton)

    @staticmethod
    def login(driver, username, password):
        LoginPage.set_username(driver,username)
        LoginPage.set_password(driver, password)
        LoginPage.click_log_in_button(driver)

