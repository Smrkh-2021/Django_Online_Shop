import json

from django.http import HttpResponse

from customers.models import Customer
from orders.models import OrderItem, Order


def save_orderitems_from_cookie_to_db(request):
    cookie_str = request.COOKIES.get('cookie_product')
    cookie_dict = json.loads(cookie_str)
    user = request.user
    customer = Customer.objects.get(user=user)
    order = Order.objects.get_or_create(customer=customer, status_id=3)[0]
    for product_id, count in cookie_dict.items():
        same_orderitems = OrderItem.objects.filter(order=order, product_id=product_id)
        if same_orderitems:
            orderitem = same_orderitems[0]
            orderitem.count += count
            orderitem.save()
        else:
            OrderItem.objects.create(order=order, product_id=product_id, count=count)
