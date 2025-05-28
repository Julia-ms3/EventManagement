from rest_framework import serializers

from events.models import Event, Participant, Registration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'location', 'organizer')


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('id', 'name', 'email', 'phone',)


class RegistrationSerializer(serializers.ModelSerializer):
    event = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True
    )
    participant = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = Registration
        fields = ('id', 'event', 'participant', 'registered_at')
