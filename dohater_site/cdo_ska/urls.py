from django.urls import path
from .views import index, HomePageView, TestCreateView, TestDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('index', index),
    path('create_test', TestCreateView.as_view(), name="create_test"),
    path('test/<int:pk>/', TestDetailView.as_view(), name="test"),
]
