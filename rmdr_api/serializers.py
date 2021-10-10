from rest_framework import serializers
from . import models


class ContextAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContextAlias
        fields = ['id']


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reminder
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = ['body']
