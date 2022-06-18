from rest_framework.routers import SimpleRouter

from django.urls import include
from django.urls import path

from authors.api import viewsets

router = SimpleRouter()
router.register('', viewsets.AuthorsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
