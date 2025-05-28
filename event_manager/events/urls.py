from django.urls import include, path
from rest_framework import routers

from events.views import EventModelViewSet

app_name = 'events'
router = routers.DefaultRouter()
router.register(r'', EventModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
