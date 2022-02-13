import imp
from unicodedata import name
from django.urls import path

app_name = "api"
from .views import ApiHome

urlpatterns = [path("", ApiHome.as_view(), name="home")]
