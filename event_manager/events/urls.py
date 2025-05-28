from django.urls import include, path
from rest_framework import routers

from events.views import EventModelViewSet, ParticipantListView, RegisterEvent

app_name = 'events'
router = routers.DefaultRouter()
router.register(r'events', EventModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterEvent.as_view()),
    path('participants/', ParticipantListView.as_view()),
]
