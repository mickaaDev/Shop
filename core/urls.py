from django.urls import path
from .views import *

urlpatterns = [
    path("", sign_in, name="sign-in"),
]