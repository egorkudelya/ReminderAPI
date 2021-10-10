from django.urls import path
from rmdr_api import views

urlpatterns = [
    path('reminder/', views.ReminderView.as_view()),
    path('reminder/<str:reminder_id>/contexts/', views.RemindCandidatesListView.as_view()),
    path('reminder/<str:reminder_id>/contexts/<str:context_id>/notifications', views.NotificationViewset.as_view())
]