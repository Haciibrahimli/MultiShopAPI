from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     UpdateAPIView,DestroyAPIView)


from my_app.models import *
from my_app.serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class SizeUpdateAPIView(UpdateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    lookup_field = 'id'

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class PartniorsDestroyAPIView(DestroyAPIView):
    queryset = Partniors.objects.all()
    serializer_class = PartniorsSerializer
    lookup_field = 'id'

class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CheckoutCreateAPIView(CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class CommentRetrieveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

class SpecialOfferDestroyAPIView(DestroyAPIView):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer
    lookup_field = 'id'

class SpecialOfferListView(ListAPIView):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer

class BasketCreateAPIView(CreateAPIView):
    queryset =Basket.objects.all()
    serializer_class =BasketSerializer

class SosialMediaUpdateAPIView(UpdateAPIView):
    queryset = SosialMedia.objects.all()
    serializer_class = SosialMediaSerializer
    lookup_field = 'id'

class ClientRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class MainDetailsDestroyAPIView(DestroyAPIView):
    queryset = MainDetails.objects.all()
    serializer_class = MainDetailsSerializer
    lookup_field = 'id'



