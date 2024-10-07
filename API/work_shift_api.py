import json

import requests

from core.api_data import ApiData


class WorkShiftApi:

    @staticmethod
    def get_all_work_shifts(access_token, parameters):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + "/shifts/"
        response = requests.request("GET", url, headers=headers, params=parameters)

        return response

    @staticmethod
    def create_work_shift(access_token, payload_data):
        payload = json.dumps(
            payload_data
        )
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + "/shifts/"
        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    @staticmethod
    def update_work_shift(access_token, payload_data, shift_id):
        payload = json.dumps(
            payload_data
        )
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f"/shifts/{shift_id}"
        response = requests.request("PUT", url, headers=headers, data=payload)

        return response

    @staticmethod
    def delete_work_shift(access_token, shift_id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f"/shifts/{shift_id}"
        response = requests.request("DELETE", url, headers=headers)
        return response

    @staticmethod
    def get_work_shift(access_token, shift_id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f"/shifts/{shift_id}"
        response = requests.request("GET", url, headers=headers)
        return response

    @staticmethod
    def get_shifts_time_periods(access_token):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f"/shifts/shifts_time_periods/all"
        response = requests.request("GET", url, headers=headers)
        return response

