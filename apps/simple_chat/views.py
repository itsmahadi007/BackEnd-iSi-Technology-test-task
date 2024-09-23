# Create your views here.
# Create your views here.
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.simple_chat.filters import ThreadFilter, MessageFilter
from apps.simple_chat.models import Thread, Message, Participant
from apps.simple_chat.serializer import ThreadDetailsSerializer, ThreadSerializer, MessageSerializer, \
    MessageDetailSerializer
from apps.users_management.models import UserManage
from backend.utils.pagination import CustomPagination


class ThreadModelView(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = ThreadFilter
    pagination_class = CustomPagination

    serializer_classes = {
        "list": ThreadDetailsSerializer,
        "retrieve": ThreadDetailsSerializer,
        "create": ThreadSerializer,
        "update": ThreadSerializer,
    }
    default_serializer_class = ThreadSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        # use this if you want to set restriction on user to see only his threads
        # return Thread.objects.filter(participants__user=self.request.user).prefetch_related(
        #     "participants",
        #     "participants__user"
        # )
        return Thread.objects.all().prefetch_related(
            "participants",
            "participants__user"
        )

    def create(self, request, *args, **kwargs):
        user1 = request.user.id
        user2 = request.data.get("user")
        if not user2:
            return Response({"error": "user field is required"}, status=400)
        # check if user2 exists
        if not UserManage.objects.filter(id=user2).exists():
            return Response({"error": "user not found"}, status=404)
        # check if exists thread between user1 and user2 exists if yes then returning it
        thread = Thread.objects.filter(participants__user_id=user1).filter(participants__user_id=user2).first()
        if thread:
            print("thread exists")
            return Response(ThreadDetailsSerializer(thread).data, status=200)
        # create new thread
        with transaction.atomic():
            thread = Thread.objects.create()
            Participant.objects.create(user_id=user1, thread=thread)
            Participant.objects.create(user_id=user2, thread=thread)
            return Response(ThreadDetailsSerializer(thread).data, status=201)


class MessageModelView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter
    pagination_class = CustomPagination

    serializer_classes = {
        "list": MessageDetailSerializer,
        "retrieve": MessageDetailSerializer,
        "create": MessageSerializer,
        "update": MessageSerializer,
    }
    default_serializer_class = MessageSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        return Message.objects.all().prefetch_related(
            "sender",
            "thread",
            "thread__participants",
            "thread__participants__user"
        ).order_by("-created_at")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def unread_messages_count(request, user_id):
    unread_messages = Message.objects.filter(thread__participants__user=user_id, is_read=False).count()
    return Response({"unread_messages": unread_messages}, status=200)
