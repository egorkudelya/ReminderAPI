from django.db import models
import uuid


class Reminder(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    regularity = models.CharField(default=1, max_length=120)

    def __str__(self):
        return self.regularity


class ContextAlias(models.Model):

    id = models.CharField(max_length=120, unique=True, primary_key=True)
    reminder = models.ForeignKey(Reminder, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Notification(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, editable=True)

    def __str__(self):
        return self.body

