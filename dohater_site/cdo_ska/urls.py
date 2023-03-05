from django.urls import path
from .views import index, home, create_test, test

urlpatterns = [
    path('', home),
    path('index', index),
    path('create_test', create_test),
    path('test', test),
]
