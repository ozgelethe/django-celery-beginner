from django.shortcuts import render
from django.http.response import HttpResponse
from .tasks import test_func
from mail.tasks import send_mail_func
# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Donen")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")