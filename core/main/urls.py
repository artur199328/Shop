from django.urls import path
from . import views
from .views import  HomeListView, ErorListView, CheckoutListView, FooterListView



urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('404/', ErorListView.as_view(), name='eror'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('checkout/', CheckoutListView.as_view(), name='checkout'),
    path('', FooterListView.as_view(), name='footer'),

    
]