"""
the script verify if the order is assigned to the zone where
the destination is located

"""
from API.order_api import OrderApis
from core.api_data import ApiData

"""
preconditions:

1 - zone with name QH_1 and polygon:
           
    33.43555761084369
    44.29401189740939
    
    33.40905185906341
    44.27032262738986
    
    33.41349392776791
    44.31598455365939

2 - zone with name QH_2 and polygon:
                                         
    33.454405803336094
    44.25869273459067


    33.41945275613843
    44.2329435280477


    33.438077033680585
    44.28907679831137

3 - no other zones assigned to this store

"""

"""
required information
"""

environment_url = ApiData.api_url

file_handler = open("order_latest_name.txt", "r")
file_content = file_handler.read()
print("the latest order name used was " + file_content)
order_id_string = input("please add new order name: ")
file_handler.close()
file_handler = open("order_latest_name.txt", "w")
file_handler.write(order_id_string)
file_handler.close()

store_id_string = input("please insert store name: ") or ApiData.dark_store
store_id_numeric = input("please insert store id: ") or 5

first_destination_latitude = input("please insert latitude of first destination: ") or 33.417042
first_destination_longitude = input("please insert longitude of first destination: ") or 44.301094
second_destination_latitude = input("please insert latitude of second destination: ") or 33.4395571
second_destination_longitude = input("please insert longitude of second destination: ") or 44.2614315

"""
functions
"""


def create_order(order_name, store_id, lat, long):
    response = OrderApis.api_create_auto_assignment_order(order_name, store_id, long, lat)
    assert response.status_code == 200, print(response.json())
    return response


"""
script
"""

# create order
response = create_order(order_name=order_id_string + "0", store_id=store_id_string, lat=first_destination_latitude,
                        long=first_destination_longitude)
assert response.json()['data']['zone']['name'] == "QH_1"
print("first order has been assigned to the right zone QH_1")

# create order
response = create_order(order_name=order_id_string + "1", store_id=store_id_string, lat=second_destination_latitude,
                        long=second_destination_longitude)
assert response.json()['data']['zone']['name'] == "QH_2"
print("second order has been assigned to the right zone QH_2")
