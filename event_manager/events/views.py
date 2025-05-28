from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from events.serializers import EventSerializer

from .models import Event, Participant, Registration
from .serializers import ParticipantSerializer, RegistrationSerializer


class EventModelViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RegisterEvent(APIView):

    def post(self, request):
        event_id = request.data.get('event_id')
        participant_data = request.data.get('participant')

        if not event_id or not participant_data:
            return Response({"error": "Event ID and participant data are required.", "required_format": {
                "event_id": "int",
                "participant": {
                    "name": "string",
                    "email": "string ",
                    "phone": "string "
                }
            }
                             }, status=status.HTTP_400_BAD_REQUEST)

        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event does not exist."}, status=status.HTTP_404_NOT_FOUND)

        if event.date < timezone.now():
            return Response({"error": "Event date has already passed. Registration closed."},
                            status=status.HTTP_400_BAD_REQUEST)

        participant_serializer = ParticipantSerializer(data=participant_data)
        if not participant_serializer.is_valid():
            return Response(participant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        participant_email = participant_data.get('email')
        participant, created = Participant.objects.get_or_create(email=participant_email,
                                                                 defaults=participant_data)

        registration_exists = Registration.objects.filter(event=event, participant=participant).exists()
        if registration_exists:
            return Response({
                "error": "Participant is already registered for this event.",
            }, status=status.HTTP_400_BAD_REQUEST)

        registration = Registration.objects.create(event=event, participant=participant)

        registration_serializer = RegistrationSerializer(registration)
        return Response(registration_serializer.data, status=status.HTTP_201_CREATED)


class ParticipantListView(ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
