from django.urls import path
from .views import hello

urlpatterns = [
    path("hello/visitor_name/<str:visitor_name>", hello, name='hello'),
]
