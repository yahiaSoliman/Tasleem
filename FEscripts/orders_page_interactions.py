from FEscripts.orders_page_selectors import OrdersPageSelectors


class OrdersPageInteractions:

    @staticmethod
    def login(driver, username, password):
        # insert username
        username_element = driver.find_element(*OrdersPageSelectors.username_selector)
        username_element.click()
        username_element.send_keys(username)

        # insert password
        password_element = driver.find_element(*OrdersPageSelectors.password_selector)
        password_element.click()
        password_element.send_keys(password)

        # click login button
        login_button_element = driver.find_element(*OrdersPageSelectors.login_button_selector)
        login_button_element.click()

    @staticmethod
    def click_create_order(driver):
        create_order_button = driver.find_element(*OrdersPageSelectors.create_order_button_selector)
        create_order_button.click()

    @staticmethod
    def insert_order_total(driver, total):
        order_total_element = driver.find_element(*OrdersPageSelectors.order_total_element)
        order_total_element.send_keys(total)

    @staticmethod
    def insert_order_id(driver, order_id):
        order_id_element = driver.find_element(*OrdersPageSelectors.order_id_selector)
        order_id_element.send_keys(order_id)

    @staticmethod
    def select_store(driver, store_id):
        store_element = driver.find_element(*OrdersPageSelectors.store_selector)
        store_element.click()
        item_element = driver.find_element(*OrdersPageSelectors.store_id_selector(store_id))
        item_element.click()

    @staticmethod
    def select_vehicle(driver, vehicle_type):
        vehicle_select_element = driver.find_element(*OrdersPageSelectors.vehicle_list_selector)
        vehicle_select_element.click()
        vehicle_list_item = driver.find_element(*OrdersPageSelectors.vehicle_type_selector(vehicle_type))
        vehicle_list_item.click()

    @staticmethod
    def insert_phone_number(driver, phone_number):
        phone_number_element = driver.find_element(*OrdersPageSelectors.phone_number_selector)
        phone_number_element.send_keys(phone_number)

    @staticmethod
    def select_order_status(driver, order_status):
        order_status_element = driver.find_element(*OrdersPageSelectors.order_status_list_selector)
        order_status_element.click()
        order_status_item = driver.find_element(*OrdersPageSelectors.order_status_value_selector(order_status))
        order_status_item.click()

    @staticmethod
    def select_merchant(driver, merchant_name):
        merchant_select_element = driver.find_element(*OrdersPageSelectors.merchant_select_selector)
        merchant_select_element.click()
        merchant_item = driver.find_element(*OrdersPageSelectors.merchant_item_selector(merchant_name))
        merchant_item.click()

    @staticmethod
    def insert_address(driver, address):
        user_address_element = driver.find_element(*OrdersPageSelectors.user_address_selector)
        user_address_element.send_keys(address)

    @staticmethod
    def click_submit(driver):
        submit_element = driver.find_element(*OrdersPageSelectors.submit_selector)
        submit_element.click()

