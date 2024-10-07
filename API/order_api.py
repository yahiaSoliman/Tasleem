import json
import requests

from core.api_data import ApiData


class OrderApis:

    @staticmethod
    def api_create_auto_assignment_order(order_id, darkstore, dest_long=44.4, dest_lat=33.4):
        payload = json.dumps({
            "order_id": order_id,
            "order_total": "2100",
            "order_bin_number": "123456",
            "order_bin_info": [
                {"324234": 123}, {"42": 123}
            ],
            "user_address": "yahia address",
            "destination_latitude": dest_lat,
            "destination_longitude": dest_long,
            "customer_phone_number": "+4232423423",
            "vehicle_type_id": 2,
            "customer_code": "1111",
            "darkstore_name": darkstore,
            "address_building": "test_building",
            "address_district": "test_district",
            "address_flat": "test_flat",
            "address_floor": "test_floor",
            "address_neighbourhood": "test_neighbourhood",
            "address_nickname": "test_nickname",
            "address_phone": "test_address_phone",
            "address_address_line1": "test_address_line1"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'secret-key': "test"
        }

        url = ApiData.api_url + '/order/auto_assignment'
        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    @staticmethod
    def api_get_order_by_id(order_id, access_token):
        payload = json.dumps({

        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/order/{order_id}'
        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    @staticmethod
    def get_all_order_statuses(access_token):
        payload = json.dumps({

        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + '/order/order_statuses/all'
        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    @staticmethod
    def cancel_order(order_id, token):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': "test"
        }

        url = ApiData.api_url + f'/order/update_order_status_internally/{order_id}'
        response = requests.request("PUT", url, headers=headers)
        assert response.status_code == 200, "can't cancel order"

    @staticmethod
    def set_ready_for_pickup_status(order_id):
        payload = json.dumps({
            "is_ready_for_pick_up_status": 1
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'secret-key': "test"
        }

        url = ApiData.api_url + f'/order/order_status/{order_id}'
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def get_order_latest_statuses(access_token, order_ids):
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        Qparams = {
            'order_ids': order_ids
        }
        url = ApiData.api_url + '/order/order_latest_statuses/'
        response = requests.request("GET", url, headers=headers, data=payload, params=Qparams)
        return response

    @staticmethod
    def get_order_details(access_token, order_id):
        payload = json.dumps({})
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'secret-key': 'test'
        }
        url = ApiData.api_url + f'/order/detail/{order_id}'
        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    @staticmethod
    def update_order_status(access_token, numeric_order_id):
        payload = json.dumps({
            "order_status_id": 4
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/order/update_order_status/{numeric_order_id}'
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response

    @staticmethod
    def get_all_orders(access_token, Qparams, timeout):
        payload = json.dumps({
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + '/order/page'
        response = requests.request("GET", url, headers=headers, data=payload, params=Qparams)

        return response

    @staticmethod
    def assign_order_manually(access_token, order_id, payload_dict):
        payload = json.dumps(payload_dict)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/order/manual_order_assignment/{order_id}'
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def unassign_order_manually(access_token, order_id, payload_dict):
        payload = json.dumps(payload_dict)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }
        url = ApiData.api_url + f'/order/manual_order_unassignment/{order_id}'
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def order_autocomplete(access_token, Qparams):
        payload = json.dumps({
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + '/order/search_autocomplete'
        response = requests.request("GET", url, headers=headers, data=payload, params=Qparams)
        return response

    @staticmethod
    def update_order_vehicle(access_token, order_numeric_id, vehicle_id):
        payload = json.dumps({
            "vehicle_type_id": vehicle_id
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + access_token
        }

        url = ApiData.api_url + f'/order/update_order_vehicle_type/{order_numeric_id}'
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response
