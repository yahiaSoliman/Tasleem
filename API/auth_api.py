import requests
import json

from core.api_data import ApiData


class AuthEndPoints:
    login_status_code = ""
    login_body = ""
    login_token = ""
    refresh_token = ""
    logout_status_code = ""
    logout_body = ""
    refresh_token_status_code = ""
    refresh_token_body = ""
    refresh_token_access_token = ""

    @staticmethod
    def api_login(user_name, password):
        payload_login = json.dumps({
            "username": user_name,
            "password": password
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        url_login = ApiData.api_url + '/auth/login'
        return requests.request("POST", url_login, headers=headers, data=payload_login)

    @staticmethod
    def api_logout(base_url, token):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/auth/logout'
        return requests.request("POST", url_login, headers=headers)

    @staticmethod
    def api_refresh_token(base_url, token):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url_login = base_url + '/auth/refresh_token'
        return requests.request("POST", url_login, headers=headers)

