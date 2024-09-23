from django.urls import path, include
from rest_framework import routers

from apps.simple_chat.views import ThreadModelView, MessageModelView, unread_messages_count

route = routers.DefaultRouter()
route.register("threads", ThreadModelView, basename="threads")
route.register("messages", MessageModelView, basename="messages")
urlpatterns = [
    path("", include(route.urls)),
    path(
        "unread_messages_count/<int:user_id>/",
        unread_messages_count,
        name="unread_messages_count",
    ),

]
