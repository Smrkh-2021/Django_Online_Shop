from datetime import timedelta

from django.test import TestCase
from ..models import Discount
from django.utils.datetime_safe import datetime


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = Discount.objects.create(value=20, type='percent', title='29 esfand')
        self.discount2 = Discount.objects.create(value=5000, type='price', title='29 esfand')
        self.discount3 = Discount.objects.create(value=30, type='percent', max_price='10000', title='29 esfand')
        self.discount4 = Discount.objects.create(value=10000, type='price', max_price='10000', title='29 esfand')
        self.discount5 = Discount.objects.create(value=20, type='percent', max_price='10000', expire_time=datetime.now().date(), title='29 esfand')
        self.discount6 = Discount.objects.create(value=7000, type='price', max_price='10000', expire_time=datetime.now().date(), title='29 esfand')
        self.discount7 = Discount.objects.create(value=20, type='percent', max_price='10000', expire_time=datetime.now().date()+timedelta(days=-1), title='noruz')
        self.discount8 = Discount.objects.create(value=15000, type='percent', expire_time=datetime.now().date()+timedelta(days=-1), title='noruz')
        self.discount9 = Discount.objects.create(value=10, type='percent', max_price='10000', expire_time=datetime.now().date()+timedelta(days=1), title='noruz')
        self.discount10 = Discount.objects.create(value=10000, type='price', expire_time=datetime.now().date()+timedelta(days=1), title='noruz')
        self.discount11 = Discount.objects.create(value=15, type='percent', max_price='10000', expire_time=datetime.now().date()+timedelta(days=2), title='noruz')
        self.discount12 = Discount.objects.create(value=15000, type='price', expire_time=datetime.now().date()+timedelta(days=2), title='noruz')


    def test1_profit_price10000(self):
        self.assertEqual(self.discount1.profit_value(10000), 2000)
        self.assertEqual(self.discount2.profit_value(10000), 5000)
        self.assertEqual(self.discount3.profit_value(10000), 3000)
        self.assertEqual(self.discount4.profit_value(10000), 10000)
        self.assertEqual(self.discount5.profit_value(10000), 2000)
        self.assertEqual(self.discount6.profit_value(10000), 7000)
        self.assertEqual(self.discount7.profit_value(10000), 0)
        self.assertEqual(self.discount8.profit_value(10000), 0)
        self.assertEqual(self.discount9.profit_value(10000), 1000)
        self.assertEqual(self.discount10.profit_value(10000), 10000)
        self.assertEqual(self.discount11.profit_value(10000), 1500)
        self.assertEqual(self.discount12.profit_value(10000), 10000)


    def test2_profit_price100000(self):
        self.assertEqual(self.discount1.profit_value(100000), 20000)
        self.assertEqual(self.discount2.profit_value(100000), 5000)
        self.assertEqual(self.discount3.profit_value(100000), 10000)
        self.assertEqual(self.discount4.profit_value(100000), 10000)
        self.assertEqual(self.discount5.profit_value(100000), 10000)
        self.assertEqual(self.discount6.profit_value(100000), 7000)
        self.assertEqual(self.discount7.profit_value(100000), 0)
        self.assertEqual(self.discount8.profit_value(100000), 0)
        self.assertEqual(self.discount9.profit_value(100000), 10000)
        self.assertEqual(self.discount10.profit_value(100000), 10000)
        self.assertEqual(self.discount11.profit_value(100000), 10000)
        self.assertEqual(self.discount12.profit_value(100000), 15000)



    def test3_profit_price7000(self):
        self.assertEqual(self.discount1.profit_value(7000), 1400)
        self.assertEqual(self.discount2.profit_value(7000), 5000)
        self.assertEqual(self.discount3.profit_value(7000), 2100)
        self.assertEqual(self.discount4.profit_value(7000), 7000)
        self.assertEqual(self.discount5.profit_value(7000), 1400)
        self.assertEqual(self.discount6.profit_value(7000), 7000)
        self.assertEqual(self.discount7.profit_value(7000), 0)
        self.assertEqual(self.discount8.profit_value(7000), 0)
        self.assertEqual(self.discount9.profit_value(7000), 700)
        self.assertEqual(self.discount10.profit_value(7000), 7000)
        self.assertEqual(self.discount11.profit_value(7000), 1050)
        self.assertEqual(self.discount12.profit_value(7000), 7000)




    def test4_profit_price7111(self):
        self.assertEqual(self.discount1.profit_value(7111), 1422)
        self.assertEqual(self.discount2.profit_value(7111), 5000)
        self.assertEqual(self.discount3.profit_value(7111), 2133)
        self.assertEqual(self.discount4.profit_value(7111), 7111)
        self.assertEqual(self.discount5.profit_value(7111), 1422)
        self.assertEqual(self.discount6.profit_value(7111), 7000)
        self.assertEqual(self.discount7.profit_value(7111), 0)
        self.assertEqual(self.discount8.profit_value(7111), 0)
        self.assertEqual(self.discount9.profit_value(7111), 711)
        self.assertEqual(self.discount10.profit_value(7111), 7111)
        self.assertEqual(self.discount11.profit_value(7111), 1066)
        self.assertEqual(self.discount12.profit_value(7111), 7111)



    def test5_profit_price2000(self):
        self.assertEqual(self.discount1.profit_value(2000), 400)
        self.assertEqual(self.discount2.profit_value(2000), 2000)
        self.assertEqual(self.discount3.profit_value(2000), 600)
        self.assertEqual(self.discount4.profit_value(2000), 2000)
        self.assertEqual(self.discount5.profit_value(2000), 400)
        self.assertEqual(self.discount6.profit_value(2000), 2000)
        self.assertEqual(self.discount7.profit_value(2000), 0)
        self.assertEqual(self.discount8.profit_value(2000), 0)
        self.assertEqual(self.discount9.profit_value(2000), 200)
        self.assertEqual(self.discount10.profit_value(2000), 2000)
        self.assertEqual(self.discount11.profit_value(2000), 300)
        self.assertEqual(self.discount12.profit_value(2000), 2000)


    def test6_str(self):
        self.assertEqual(self.discount1.__str__(), '29 esfand: 20 percent')
        self.assertEqual(self.discount2.__str__(), '29 esfand: 5000 price')
        self.assertEqual(self.discount3.__str__(), '29 esfand: 30 percent')
        self.assertEqual(self.discount4.__str__(), '29 esfand: 10000 price')
        self.assertEqual(self.discount5.__str__(), '29 esfand: 20 percent')
        self.assertEqual(self.discount6.__str__(), '29 esfand: 7000 price')
        self.assertEqual(self.discount7.__str__(), 'noruz: 20 percent')
        self.assertEqual(self.discount8.__str__(), 'noruz: 15000 percent')
        self.assertEqual(self.discount9.__str__(), 'noruz: 10 percent')
        self.assertEqual(self.discount10.__str__(), 'noruz: 10000 price')
        self.assertEqual(self.discount11.__str__(), 'noruz: 15 percent')
        self.assertEqual(self.discount12.__str__(), 'noruz: 15000 price')