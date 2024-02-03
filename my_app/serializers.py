from rest_framework import serializers
from my_app.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Color
        fields = "__all__"

class SizeSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Size
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Product
        fields = "__all__"

class PartniorsSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Partniors
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Contact
        fields = "__all__"


class CheckoutSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Checkout
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProductImage
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Comment
        fields = "__all__"


class SpecialOfferSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = SpecialOffer 
        fields = "__all__"


class SliderOfferSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Slider 
        fields = "__all__"


class BasketSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Basket
        fields = "__all__"


class SosialMediaSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = SosialMedia
        fields = "__all__"


class MainDetailsSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = MainDetails
        fields = "__all__"
