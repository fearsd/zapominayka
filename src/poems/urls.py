from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from poems.api import viewsets

router = SimpleRouter()

router.register('screens', viewsets.ScreensViewSet)
router.register('', viewsets.PoemsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
