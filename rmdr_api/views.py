from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import ContextAlias, Reminder, Notification
from rest_framework import status
import requests


class ReminderView(APIView):

    def get(self, request):
        contexts = Reminder.objects.all()
        serializer = serializers.ReminderSerializer(contexts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemindCandidatesListView(APIView):

    def get(self, request, reminder_id):
        contexts = ContextAlias.objects.filter(reminder__id=reminder_id)
        serializer = serializers.ContextAliasSerializer(contexts, many=True)
        return Response(serializer.data)

    def post(self, request, reminder_id):
        try:
            Reminder.objects.get(pk=reminder_id)
        except Reminder.DoesNotExist:
            raise Http404

        serializer = serializers.ContextAliasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(reminder_id=reminder_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationViewset(APIView):

    def __get_backlog_for_user(self, context_id):
        int_port = f'http://127.0.0.1:8000/contexts/{context_id}/'
        response = requests.get(int_port)
        if response.status_code == 200:
            data = response.json()
            # print(data)
            return [user_data for user_data in data if user_data['events'] is not None]
        return None

    def save_user_log(self):
        for context in ContextAlias.objects.all():
            current_id = context.id
            user_log = self.__get_backlog_for_user(current_id)
            if user_log:
                for user_data in user_log:
                    notification = Notification.objects.create(body=user_data)
                    notification.save()


    def get(self, request, **kwargs):  # for demonstration
        notifications = Notification.objects.all()
        serializer = serializers.NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
