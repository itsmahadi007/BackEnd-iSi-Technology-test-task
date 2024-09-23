from django.apps import apps
from django.contrib import admin
from django.contrib.auth.models import Group
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Register your models here.


for model in apps.get_app_config("users_management").models.values():
    admin.site.register(model)

for model in apps.get_app_config("allauth").models.values():
    admin.site.unregister(model)

for model in apps.get_app_config("dj_rest_auth").models.values():
    admin.site.unregister(model)

for model in apps.get_app_config("rest_framework_simplejwt").models.values():
    admin.site.unregister(model)

admin.site.unregister(Group)
admin.site.unregister(PeriodicTask)
admin.site.unregister(CrontabSchedule)
