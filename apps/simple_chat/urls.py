from django.urls import path, include
from rest_framework import routers

from apps.users_management.views import ThreadModelView, MessageModelView

route = routers.DefaultRouter()
route.register("threads", ThreadModelView, basename="threads")
route.register("messages", MessageModelView, basename="messages")
urlpatterns = [
    path("", include(route.urls)),
]
