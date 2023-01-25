from django.urls import path
from .views import index, first, second, third, third_post


urlpatterns = [
    path("", index),
    path("first/", first),
    path("second/", second),
    path("third/", third),
    path("thirdpost/", third_post),
]
