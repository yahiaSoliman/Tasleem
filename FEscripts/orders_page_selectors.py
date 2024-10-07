from selenium.webdriver.common.by import By


class OrdersPageSelectors:
    username_selector = (By.XPATH, "(//input)[1]")
    password_selector = (By.XPATH, "(//input)[2]")
    login_button_selector = (By.XPATH, "//button[@type='submit']")
    create_order_button_selector = (By.XPATH, "//button[text()='Create Order']")
    order_total_element = (By.XPATH, "//label[text()='Order Total']/following-sibling::input")
    order_id_selector = (By.XPATH, "//label[text()='Order ID']/following-sibling::input")
    store_selector = (By.XPATH, "//div[@class='multiselect']")
    item_selector = (By.XPATH, "//span[text()='Stores - TG']")
    vehicle_list_selector = (By.XPATH, "//label[text()='Vehicle']/following-sibling::div")
    phone_number_selector = (By.XPATH, "//label[text()='Phone number']/following-sibling::input")
    order_status_list_selector = (By.XPATH, "//label[text()='Order Status']/following-sibling::div")
    merchant_select_selector = (By.XPATH, "//label[text()='ERP Next Merchant']/following-sibling::div")
    merchant_item_selector = lambda merchant_name: (By.XPATH, f"//span[text()='{merchant_name}']")
    user_address_selector = (By.XPATH, "//label[text()='User Address']/following-sibling::input")
    submit_selector = (By.XPATH, "//button[text()='Create']")
    store_id_selector = lambda store_id: (By.XPATH, f"//span[text()='{store_id}']")
    vehicle_type_selector = lambda vehicle_type: (By.XPATH, f"//span[text()='{vehicle_type}']")
    order_status_value_selector = lambda order_status: (By.XPATH, f"//span[text()='{order_status}']")
