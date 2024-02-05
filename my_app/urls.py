from django.urls import path
from my_app.views import *

urlpatterns = [
    path("", CategoryListView.as_view(), name='category-list'),
    path("color/create/", ColorCreateAPIView.as_view(), name='color-list'),
    path("size/update/<id>/", SizeUpdateAPIView.as_view(), name='size-update'),
    path("product/retrieve", ProductRetrieveAPIView.as_view(), name='product-retrieve'),
    path("partnior/destroy",PartniorsDestroyAPIView.as_view(), name='partnior-destroy'),
    path("contact/list",ContactListView.as_view(), name='contact-list'),
    path("checkout/create",CheckoutCreateAPIView.as_view(), name='checkout-create'),
    path("product/update",ProductUpdateAPIView.as_view(), name='product-update'),
    path("comment/retrieve'",CommentRetrieveAPIView.as_view(), name='comment-retrieve'),
    path("special/offer/delate",SpecialOfferDestroyAPIView.as_view(), name='special-offer-delate'),
    path("special/offer/list",SpecialOfferListView.as_view(), name='special-offer-list'),
    path("basket/create",BasketCreateAPIView.as_view(), name='basket-create'),
    path("sosial/media",SosialMediaUpdateAPIView.as_view(), name='sosial-media'),
    path("client/retrieve",ClientRetrieveAPIView.as_view(), name='client-retrieve'),
    path("main/detail/destroy",MainDetailsDestroyAPIView.as_view(), name='main-detail-destroy'),
]