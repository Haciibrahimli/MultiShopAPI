from django.urls import path
from my_app.views import *

urlpatterns = [
    path("",CategoryListView.as_view(), name='category-list'),
    path("color/create/<id>", ColorListAPIView.as_view(), name='color-list'),
    path("size/update/<id>", SizeListAPIView.as_view(), name='size-update'),
    path("product/retrieve/<id>", ProductRetrieveAPIView.as_view(), name='product-retrieve'),
    path("partnior/destroy/<id>",PartniorsListAPIView.as_view(), name='partnior-destroy'),
    path("contact/list",ContactListView.as_view(), name='contact-list'),
    path("checkout/create",CheckoutCreateAPIView.as_view(), name='checkout-create'),
    path("product/update/<id>",ProductCreateAPIView.as_view(), name='product-update'),
    path("comment/retrieve/<id>/'",CommentCreateAPIView.as_view(), name='comment-retrieve'),
    path("special/offer/delate/<id>",SpecialOfferDestroyAPIView.as_view(), name='special-offer-delate'),
    path("special/offer/list",SpecialOfferUpdateAPIView.as_view(), name='special-offer-list'),
    path("basket/create",BasketCreateAPIView.as_view(), name='basket-create'),
    path("sosial/media/<id>",SosialMediaUpdateAPIView.as_view(), name='sosial-media'),
    path("client/retrieve/<id>",ClientRetrieveAPIView.as_view(), name='client-retrieve'),
    path("main/detail/destroy/<id>",MainDetailsRetrieveAPIView.as_view(), name='main-detail-destroy'),
]