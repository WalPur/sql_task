from django.urls import include, path
from first_task.api.views import RecordsViewSet, first, index, second, third, third_post
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", RecordsViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
