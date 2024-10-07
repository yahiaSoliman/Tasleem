from selenium.webdriver.common.by import By


class DarkstorePageSelectors:
    store_name_selector = lambda store_name: (By.XPATH, f"//td[text()='{store_name}']")
    settings_icon_selector = lambda store_name: (By.XPATH, f"//td[text()='{store_name}']/following::a")
    stop_auto_assignment_checkbox_selector = (By.XPATH, "//div[text()='Stop Auto Assignment']")
    save_changes_button = (By.XPATH, "//button[text()='Save changes']")

