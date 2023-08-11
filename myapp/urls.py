from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import VehicleList, VehicleUpdate, CustomLoginView, RegisterView

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('list/', VehicleList.as_view(), name='vehicle'),
    path('update/<int:pk>/',VehicleUpdate.as_view(),name='vehicle-update'),


]
