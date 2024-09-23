from rest_framework import serializers

from apps.simple_chat.models import Thread, Message, Participant
from apps.users_management.serializer.user_serializer import UserSerializer


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = "__all__"


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"


class ParticipantDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Participant
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ThreadDetailsSerializer(serializers.ModelSerializer):
    participants = ParticipantDetailSerializer(many=True)

    class Meta:
        model = Thread
        fields = "__all__"


class MessageDetailSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = "__all__"
