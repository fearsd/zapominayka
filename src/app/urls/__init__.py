from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import include
from django.urls import path

api = [
    path('v1/', include('app.urls.v1', namespace='v1')),
]


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Everything is ok')


urlpatterns = [
    path('', hello),
    path('admin/', admin.site.urls),
    path('api/', include(api)),
]
