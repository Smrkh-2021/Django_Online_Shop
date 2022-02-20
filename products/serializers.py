# from rest_framework import serializers
from .models import Product, Discount, Category, Brand



# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'



# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     discount = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all())
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
#     name = serializers.CharField()
#     weight = serializers.CharField()
#     dimension = serializers.CharField()
#     color = serializers.CharField()
#     count = serializers.IntegerField()
#     price = serializers.IntegerField()
#
#
#     def update(self, instance: Product, validated_data: dict) -> Product:
#         instance.discount = validated_data.get('discount', instance.discount)
#         instance.category = validated_data.get('category', instance.category)
#         instance.brand = validated_data.get('brand', instance.brand)
#         instance.name = validated_data.get('name', instance.name)
#         instance.weight = validated_data.get('weight', instance.weight)
#         instance.dimension = validated_data.get('dimension', instance.dimension)
#
#         return instance
#
#     def create(self, validated_data: dict) -> Product:
#         return Product.objects.create(**validated_data)