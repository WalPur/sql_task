from django.urls import path
from .views import index, first, second


urlpatterns = [
    path("", index),
    path("first/", first),
    path("second/", second),
]
