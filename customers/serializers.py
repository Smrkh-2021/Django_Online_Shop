from rest_framework import serializers

from core.models import User
from customers.models import Address, Customer





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    # customer_set = serializers.HyperlinkedModelSerializer(viewname='',queryset=Customer.objects.all(), many=True)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'