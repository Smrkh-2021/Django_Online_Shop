import json

from .models import OrderItem


def set_cart_cookie(request):
    id_product = request.data['product']
    count_product = int(request.data['count'])
    cookie_product = request.COOKIES.get('cookie_product')
    if cookie_product:
        cookie_dict = json.loads(cookie_product)
        if id_product in cookie_dict.keys():
            cookie_dict[id_product] = cookie_dict[id_product] + count_product
            return json.dumps(cookie_dict)
        cookie_dict[id_product] = count_product
        return json.dumps(cookie_dict)
    return json.dumps({id_product: count_product})


def list_of_orderitems_from_cookie(request):
    cookie_dict = request.COOKIES.get('cookie_product')
    orderitem_list = []
    try:
        json_cook = json.loads(cookie_dict)
        for product_id, count in json_cook.items():
            orderitem = OrderItem(product_id=product_id, count=count)
            orderitem_list.append(orderitem)
    except:
        orderitem_list = []
    return orderitem_list


def number_of_orderitems_in_cookie(request):
    cookie_str = request.COOKIES.get('cookie_product')
    if not cookie_str:
        return 1
    cookie_dict = json.loads(cookie_str)
    product_id = request.data['product']
    if cookie_dict.get(product_id):
        return len(cookie_dict)
    return len(cookie_dict) + 1