from django.urls import path
from my_app.views import *

urlpatterns = [
    path("", GYMListView.as_view(), name='gym-list'),
    path("gymcreated/", GYMCreateAPIView.as_view(), name='gym-created'),
    path("gymupdate/<id>/", GYMUpdateAPIView.as_view(), name='update'),
    path("gym/<id>/", GYMRetrieveAPIView.as_view(), name='detail'),
    path("gymdelate/<id>/", GYMDestroyAPIView.as_view(), name='delate'),

    path("trainercreated/", TrainerCreateAPIView.as_view(), name='trainer-created'),
    path("trainerupdate/<id>/", TrainerUpdateAPIView.as_view(), name='update'),
    path("trainer/<id>/", TrainerRetrieveAPIView.as_view(), name='detail'),
    path("trainerdelate/<id>/", TrainerDestroyAPIView.as_view(), name='delate'),

    path("clientcreated/", ClientCreateAPIView.as_view(), name='trainer-created'),
    path("clientupdate/<id>/", ClientUpdateAPIView.as_view(), name='update'),
    path("client/<id>/", ClientRetrieveAPIView.as_view(), name='detail'),
    path("clientdelate/<id>/", ClientDestroyAPIView.as_view(), name='delate'),
 
    path("workoutsessioncreated/", WorkoutSessionCreateAPIView.as_view(), name='trainer-created'),
    path("workoutsessionupdate/<id>/", WorkoutSessionUpdateAPIView.as_view(), name='update'),
    path("workoutsession/<id>/", WorkoutSessionRetrieveAPIView.as_view(), name='detail'),
    path("workoutsessiondelate/<id>/", WorkoutSessionDestroyAPIView.as_view(), name='delate'),




]