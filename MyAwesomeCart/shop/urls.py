from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='shopHome'),
    path('about/', views.about, name='aboutUs'),
    path('contact/', views.contact, name='contact'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('productview/', views.productview, name='productview'),
    path('checkout/', views.checkout, name='checkout'),
]

