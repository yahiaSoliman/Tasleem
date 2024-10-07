import json
import requests

from core.api_data import ApiData


class DarkStoreApis:
    response = ""

    @staticmethod
    def api_get_all_darkstore(access_token, page_number, per_page):
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        Qparams = {
            'page_number': page_number,
            'per_page': per_page
        }
        url = ApiData.api_url + '/dark_stores/page'
        response = requests.request("GET", url, headers=headers, data=payload, params=Qparams)

        return response

    @staticmethod
    def api_get_darkstore(access_token, darkstorrid):
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/dark_stores/{darkstorrid}'
        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    @staticmethod
    def api_update_store_settings(access_token, store_id, setting_text):
        payload = json.dumps(setting_text)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/darkstore_settings/{store_id}'

        response = requests.request("PUT", url, headers=headers, data=payload)

        return response
