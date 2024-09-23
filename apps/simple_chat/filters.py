from datetime import datetime

from django_filters import rest_framework as filters

from apps.simple_chat.models import Thread, Message


class ThreadFilter(filters.FilterSet):
    participants = filters.CharFilter(method="filter")
    date_range = filters.CharFilter(method="filter")

    class Meta:
        model = Thread
        fields = [
            "id",
            "participants",
            "date_range"
        ]

    @staticmethod
    def filter(queryset, name, value):
        if name == "participants":
            return queryset.filter(participants__user_id=value)
        elif name == "date_range":
            # expected format: "2021-01-01,2021-01
            start_date_str, end_date_str = [s.strip() for s in value.split(",")]
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            return queryset.filter(
                created_at__range=[start_date, end_date]
            )
        else:
            return None


class MessageFilter(filters.FilterSet):
    thread = filters.CharFilter(method="filter")
    sender = filters.CharFilter(method="filter")
    receiver = filters.CharFilter(method="filter")
    date_range = filters.CharFilter(method="filter")

    class Meta:
        model = Message
        fields = [
            "id",
            "thread",
            "sender",
            "receiver",
            "is_read",
            "date_range"
        ]

    @staticmethod
    def filter(queryset, name, value):
        if name == "thread":
            return queryset.filter(thread_id=value)
        elif name == "sender":
            return queryset.filter(sender_id=value)
        elif name == "receiver":
            return queryset.filter(thread__participants__user_id=value)
        elif name == "date_range":
            # expected format: "2021-01-01,2021-01
            start_date_str, end_date_str = [s.strip() for s in value.split(",")]
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            return queryset.filter(
                created_at__range=[start_date, end_date]
            )
        else:
            return None
