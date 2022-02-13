from django.test import TestCase
from ..models import Discount


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = Discount.objects.create()
