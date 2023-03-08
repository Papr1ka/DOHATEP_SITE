from django.urls import path
from .views import index, HomePageView, create_test, test

urlpatterns = [
    path('', HomePageView.as_view()),
    path('index', index),
    path('create_test', create_test),
    path('test', test),
]
