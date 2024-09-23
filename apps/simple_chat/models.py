from django.db import models

from apps.users_management.models import UserManage


# Create your models here.
class Thread(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Thread: {self.id} - Created at: {self.created_at}"


class Participant(models.Model):
    user = models.ForeignKey(UserManage, on_delete=models.CASCADE, related_name="participants")
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="participants")

    def __str__(self):
        return f"Participant: {self.user.username} - Thread: {self.thread.id}"


class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(UserManage, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Message: {self.id} - Thread: {self.thread.id} - Sender: {self.sender.username}"
