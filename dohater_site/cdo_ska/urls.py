from django.urls import path
from .views import index, HomePageView, create_test, TestDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('index', index),
    path('create_test', create_test),
    path('test/<int:pk>/', TestDetailView.as_view(), name="test"),
]
