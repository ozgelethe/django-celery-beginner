from celery.schedules import crontab
from django.shortcuts import render
from django.http.response import HttpResponse
from .tasks import test_func
from mail.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
from django.utils import timezone
import uuid

# Create your views here.

def test(request):
    
    test_func.delay()
    
    return HttpResponse("Donen")

def send_mail_to_all(request):
    
    send_mail_func.delay()
    
    return HttpResponse("Sent")

def schedule_mail(request):
    
    # Create a unique name for the task using a timestamp and a UUID
    task_name = f"schedule_mail_task_{timezone.now().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"

    # Create a CrontabSchedule object if it doesn't exist
    schedule, created = CrontabSchedule.objects.get_or_create(minute=6, hour=23)

    # Create the PeriodicTask with the unique name
    task = PeriodicTask.objects.create(crontab=schedule, name=task_name, task='mail.tasks.send_mail_func')

    # schedule, created = CrontabSchedule.objects.get_or_create(minute=1, hour=18,)
    # task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_" + "5", task='mail.tasks.send_mail_func') #, args = json.dumps((2,3))
    
    return HttpResponse("Dones")