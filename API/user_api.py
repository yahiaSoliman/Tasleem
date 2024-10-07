import json

import requests

from core.api_data import ApiData
from core.base_class_api import BaseApiClass


class UserApi:

    @staticmethod
    def get_roles(access_token):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + '/roles/page'
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def invite_user(access_token, bodyData):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + '/users/invite'
        response = requests.request("POST", url, headers=headers, data=json.dumps(bodyData))
        return response

    @staticmethod
    def invite_check_user(parameters, body):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        url = ApiData.api_url + '/users/invite/check'
        response = requests.request("POST", url, headers=headers, params=parameters, data=json.dumps(body))
        return response

    @staticmethod
    def change_user_password(access_token, user_id, body):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f'/users/change_password/{user_id}'
        response = requests.request("POST", url, headers=headers, data=json.dumps(body))
        return response

    @staticmethod
    def get_all_users(access_token, parameters):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + '/users/page'
        response = requests.request("GET", url, params=parameters, headers=headers)
        return response

    @staticmethod
    def get_user_data(access_token, user_id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/users/{user_id}'
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def update_user_data(access_token, user_id, body):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/users/{user_id}'
        response = requests.request("PUT", url, headers=headers, data=json.dumps(body))
        return response

    @staticmethod
    def user_request_new_password(user_email):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        url = ApiData.api_url + "/users/reset_password"
        response = requests.request("POST", url, headers=headers, data=json.dumps({"user_email": user_email}))
        return response

    @staticmethod
    def deactivate_user(access_token, user_id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f"/users/deactivate/{user_id}"
        response = requests.request("POST", url, headers=headers)
        return response

    @staticmethod
    def activate_user(access_token, user_id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f"/users/activate/{user_id}"
        response = requests.request("POST", url, headers=headers)
        return response
