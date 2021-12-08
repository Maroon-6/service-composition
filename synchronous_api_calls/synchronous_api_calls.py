import requests
import json

endpoint = "local_host_url"
urls = [
    endpoint + "/orders",
    endpoint + "/orders/users"
]


def get_all_order_ids_by_user_id(user_id):
    url = urls[1] + '/' + str(user_id)
    rsp = requests.get(url)
    data = json.loads(rsp.content)
    order_ids = []
    for d in data:
        order_ids.append(d['order_id'])

    return order_ids


def price_sum_orders_type(order_type, order_ids):
    price_sum = 0
    for order_id in order_ids:
        url = urls[0] + '/' + str(order_id)
        rsp = requests.get(url)
        data = json.loads(rsp.content)
        if data['status'] == order_type:
            price_sum += data['total_price']

    return price_sum


# Normal coding with synchronous API calls.
# Configuration: user_id & order_type
def sync_driver(user_id, order_type):
    orders_ids = get_all_order_ids_by_user_id(user_id)
    price_sum = price_sum_orders_type(order_type, orders_ids)
    print("The price sum of " + order_type + " orders for user_id: " + str(user_id) + " is " + str(price_sum))


# Tests

sync_driver(3, "PENDING")
sync_driver(3, "CANCELLED")
sync_driver(3, "COMPLETE")
sync_driver(1, "COMPLETE")
