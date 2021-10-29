from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('about/', views.about),
    path('shop/', views.shop),

]