import json

import requests

from core.api_data import ApiData


class VehicleAPI:

    @staticmethod
    def create_vehicle(access_token, payload_dict):
        payload = json.dumps(payload_dict)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + "/vehicles/"
        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    @staticmethod
    def get_all_vehicle_types():
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'secret-key': 'test'
        }
        url = ApiData.api_url + "/vehicles/vehicle_types/all"
        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    @staticmethod
    def activate_vehicle(access_token, vehicle_id, flag_value):
        payload = json.dumps({
            "activate": flag_value
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/vehicles/activate_deactivate/{vehicle_id}'
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response

    @staticmethod
    def get_vehicle(access_token, vehicle_id):
        payload = json.dumps({
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f'/vehicles/{vehicle_id}'
        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    @staticmethod
    def delete_vehicle(access_token, vehicle_id):
        payload = json.dumps({
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f"/vehicles/{vehicle_id}"
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response

    @staticmethod
    def update_vehicle(access_token, vehicle_id, payload_dict):
        payload = json.dumps(payload_dict)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f"/vehicles/{vehicle_id}"
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response
