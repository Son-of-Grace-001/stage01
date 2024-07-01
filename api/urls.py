from django.urls import path
from .views import hello

urlpatterns = [
    path('hello/visitor_names =/<str:visitor_name>/', hello, name='hello'),
]
