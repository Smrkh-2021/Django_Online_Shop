import json

from customers.models import Customer
from orders.models import Order


def orderitem_num(request):
    if request.user.is_anonymous:
        cookie_str = request.COOKIES.get('cookie_product')
        if cookie_str:
            cookie_dict = json.loads(cookie_str)
            orderitem_num = len(cookie_dict)
            return {
                    'orderitem_num': orderitem_num
            }
        else:
            return {
                    'orderitem_num': 0
            }

    else:
        user = request.user
        customer = Customer.objects.get(user=user)
        try:
            order = Order.objects.get(customer=customer, status_id=3)
        except:
            return {
                'orderitem_num': 0
            }
        orderitem_num = len(order.orderitem_set.all())
        return {
            'orderitem_num': orderitem_num
        }