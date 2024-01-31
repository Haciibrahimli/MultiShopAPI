from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     UpdateAPIView,DestroyAPIView)


from my_app.models import *
from my_app.serializers import *


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

class GYMDestroyAPIView(DestroyAPIView):
    queryset = GYM.objects.all()
    serializer_class = GYMSerializer
    lookup_field = 'id'

class TrainerListView(ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerCreateAPIView(CreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerUpdateAPIView(UpdateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    lookup_field = 'id'

class TrainerRetrieveAPIView(RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    lookup_field = 'id'

class TrainerDestroyAPIView(DestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = GYMSerializer
    lookup_field = 'id'

class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdateAPIView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'

class ClientRetrieveAPIView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'

class ClientDestroyAPIView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'

class WorkoutSessionListView(ListAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer

class WorkoutSessionCreateAPIView(CreateAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer

class WorkoutSessionUpdateAPIView(UpdateAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    lookup_field = 'id'

class WorkoutSessionRetrieveAPIView(RetrieveAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    lookup_field = 'id'

class WorkoutSessionDestroyAPIView(DestroyAPIView):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    lookup_field = 'id'
