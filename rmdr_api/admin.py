from django.contrib import admin
from rmdr_api.models import ContextAlias, Reminder, Notification


admin.site.register(ContextAlias)
admin.site.register(Reminder)
admin.site.register(Notification)
