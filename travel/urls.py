from django.urls import path
from . import views


urlpatterns = [
    path('', views.travel_home, name="travel-home"),
    path('add_destination/', views.add_destination, name="add-destination"),
]

