from allauth.account.models import EmailAddress
from django.core.management.base import BaseCommand

from apps.simple_chat.models import Thread, Participant, Message
from apps.users_management.models import UserManage


class Command(BaseCommand):
    help = "Add Sample Data"

    @staticmethod
    def create_superuser(username, password, email, first_name, last_name, user_type):
        users = UserManage.objects.filter(username=username)
        if users.exists():
            print("User " + username + " already exists")
            return
        user_obj = UserManage.objects.create_user(
            is_superuser=True,
            is_active=True,
            is_staff=True,
            username=username,
            password=password,
            email=email,
            email_verified=True,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
        )

        EmailAddress.objects.create(
            user=user_obj,
            email=email,
            verified=True,
            primary=True,
        )

        print("User " + username + " successfully created")
        return user_obj

    def handle(self, *args, **options):
        # Create superusers
        admin_user = self.create_superuser(
            username="admin",
            password="1516",
            email="mh@mahadihassan.com",
            first_name="",
            last_name="",
            user_type="admin",
        )

        mahadi_user = self.create_superuser(
            username="mahadi",
            password="1516",
            email="me.mahadi10@gmail.com",
            first_name="Mahadi",
            last_name="Hassan",
            user_type="admin",
        )

        user1 = self.create_superuser(
            username="user1",
            password="password1",
            email="user1@example.com",
            first_name="User",
            last_name="One",
            user_type="user",
        )

        user2 = self.create_superuser(
            username="user2",
            password="password2",
            email="user2@example.com",
            first_name="User",
            last_name="Two",
            user_type="user",
        )

        print("Superusers and additional users created")

        # Creating sample threads, participants, and messages
        try:
            print("Creating sample data...")

            # Create thread 1
            thread1 = Thread.objects.create()

            # Add participants
            Participant.objects.create(user=admin_user, thread=thread1)
            Participant.objects.create(user=user1, thread=thread1)

            # Create messages for thread 1
            Message.objects.create(thread=thread1, sender=admin_user, text="Hello from admin!")
            Message.objects.create(thread=thread1, sender=user1, text="Hello from user1!")
            Message.objects.create(thread=thread1, sender=admin_user, text="How are you doing?")
            Message.objects.create(thread=thread1, sender=user1, text="I'm doing great, thanks!")
            Message.objects.create(thread=thread1, sender=admin_user, text="Glad to hear!")

            # Create thread 2
            thread2 = Thread.objects.create()

            # Add participants to thread 2
            Participant.objects.create(user=mahadi_user, thread=thread2)
            Participant.objects.create(user=user2, thread=thread2)

            # Create messages for thread 2
            Message.objects.create(thread=thread2, sender=mahadi_user, text="Hi from Mahadi!")
            Message.objects.create(thread=thread2, sender=user2, text="Hi from user2!")
            Message.objects.create(thread=thread2, sender=mahadi_user, text="How's your day?")
            Message.objects.create(thread=thread2, sender=user2, text="It's been productive, what about yours?")
            Message.objects.create(thread=thread2, sender=mahadi_user, text="Busy, but good!")

            print("Sample data created successfully")
        except Exception as e:
            print(f"Error in creating data: {e}")
