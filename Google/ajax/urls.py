from django.urls import path
from .views import *

urlpatterns = [
    path('usernames/', usernames.as_view),
    path('emails/', emails.as_view),
]
