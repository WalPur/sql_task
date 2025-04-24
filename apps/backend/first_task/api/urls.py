from django.urls import include, path
from first_task.api.views import EmailViewSet, RecordsViewSet, second, third
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("second_task", RecordsViewSet)
router.register("third_task", EmailViewSet)
urlpatterns = [
    path("api/", include(router.urls)),
    path("template/second", second),
    path("template/third", third),
]
