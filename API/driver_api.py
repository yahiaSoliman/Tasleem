import requests
import json

from core.api_data import ApiData


class DriverEndPoints:
    drivers_page_status_code = ""
    drivers_page_body = ""

    @staticmethod
    def api_drivers_page(base_url, token):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/page'
        return requests.request("GET", url_login, headers=headers)

    @staticmethod
    def api_drivers_search_autocomplete(base_url, token, search, per_page, page):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        params = {
            'query': search,
            'per_page': per_page,
            'page': page
        }
        url_login = base_url + '/drivers/search_autocomplete'
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_drivers_clocked_in_locations(base_url, token, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/clocked_in/locations'
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_driver_orders_history(base_url, token, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/driver_orders_history'
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_driver_driver_id(base_url, token, driver_id, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/' + str(driver_id)
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_driver_statuses_all(base_url, token, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/driver_statuses/all'
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_driver_status_updates_page(base_url, token, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/driver_status_updates/page'
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_driver_failed_delivery_reasons(base_url, token, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/failed_delivery/reasons'
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_driver_driver_clock_in_loc_driver_id(base_url, token, driver_id, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/driver_clock_in_loc/' + str(driver_id)
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_driver_driver_clock_out_loc_driver_id(base_url, token, driver_id, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/driver_clock_in_loc/' + str(driver_id)
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_driver_driver_clock_out_status_driver_id(base_url, token, driver_id, params):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/drivers/driver_clock_out_status/' + str(driver_id)
        return requests.request("GET", url_login, headers=headers, params=params)

    @staticmethod
    def api_get_fairness_scores(access_token, store_id, vehicle_type_id):
        Qparams = {
            'dark_store_id': store_id,
            'vehicle_type_id': vehicle_type_id
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + '/drivers/next_assigned_drivers/sorted'
        response = requests.request("GET", url, headers=headers, params=Qparams)
        return response

    @staticmethod
    def api_force_clock_out(access_token, driver_id):
        Qparams = {
            'is_manual': False
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f'/drivers/force_clock_out/{driver_id}'
        response = requests.request("POST", url, headers=headers, params=Qparams)
        return response
