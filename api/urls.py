from django.urls import path
from .views import hello

urlpatterns = [
    path("api/hello/<str:visitor_name>/", hello, name='hello'),
]
