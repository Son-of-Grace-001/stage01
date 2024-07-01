from django.urls import path
from . import views


urlpatterns = [
  path('hello?visitor_name= /<str:visitor_name', views.stageone),
]