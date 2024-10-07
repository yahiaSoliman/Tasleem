import json

import requests

from core.api_data import ApiData


class ZoneAPI:
    @staticmethod
    def create_zone(access_token, payload_dict):
        payload = json.dumps(payload_dict)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + "/zones/"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def get_zone(access_token, zone_id):
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f"/zones/{zone_id}"
        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    @staticmethod
    def update_zone(access_token, zone_id, payload_dict):
        payload = json.dumps(payload_dict)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f"/zones/{zone_id}"
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response

    @staticmethod
    def delete_zone(access_token, zone_id):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f"/zones/{zone_id}"
        response = requests.request("DELETE", url, headers=headers)
        return response

    @staticmethod
    def get_all_zones(access_token, Qparams):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f"/zones/page"
        response = requests.request("GET", url, headers=headers, params=Qparams)
        return response

    @staticmethod
    def assign_darkstore_to_zone(access_token, darkstore_id, zone_id):
        payload = json.dumps({
            "dark_store_id": darkstore_id
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f"/zones/assign/{zone_id}"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def unassign_darkstore_to_zone(access_token, darkstore_id, zone_id):
        payload = json.dumps({
            "dark_store_id": darkstore_id
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f"/zones/un_assign/{zone_id}"
        response = requests.request("POST", url, headers=headers, data=payload)
        return response
