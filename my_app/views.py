from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     UpdateAPIView,DestroyAPIView)


from my_app.models import *
from my_app.serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [AllowAny]

class SizeCreateAPIView(CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = [AllowAny]
   

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class PartniorsListAPIView(ListAPIView):
    queryset = Partniors.objects.all()
    serializer_class = PartniorsSerializer
    lookup_field = 'id'

class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CheckoutCreateAPIView(CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [AllowAny]

class ProductCreateAPIView(CreateAPIView): #CreateApi ce ListApi de  "id" lazim deyil
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
   

class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProducRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
  

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

class SpecialOfferDestroyAPIView(DestroyAPIView):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer
    lookup_field = 'id'

class SpecialOfferUpdateAPIView(UpdateAPIView):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer

class BasketCreateAPIView(CreateAPIView):
    queryset =Basket.objects.all()
    serializer_class =BasketSerializer
    permission_classes = [AllowAny]

class SosialMediaUpdateAPIView(UpdateAPIView):
    queryset = SosialMedia.objects.all()
    serializer_class = SosialMediaSerializer
    lookup_field = 'id'

class ClientRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class MainDetailsRetrieveAPIView(DestroyAPIView):
    queryset = MainDetails.objects.all()
    serializer_class = MainDetailsSerializer
    lookup_field = 'id'



