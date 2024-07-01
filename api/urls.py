from django.urls import path
from . import views


urlpatterns = [
  path('api/hello?visitor_name=<str:visitor_name', views.stageone),
]