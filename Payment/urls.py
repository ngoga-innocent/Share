from django.urls import path
from .views import payment_page
from . import views
urlpatterns = [
   
    path('',payment_page,name='payment'),
    path('create-payment-intent/', views.create_payment_intent, name='create_payment_intent'),
    ]
