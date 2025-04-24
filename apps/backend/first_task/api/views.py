from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Avg, Sum
from django.http import HttpResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from first_task.api.serializers import RecordInputSerializer, RecordsSerializer
from first_task.models import Mails, Record_names, Records
from first_task.selectors import get_second_task_data
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


def index(request):
    return HttpResponse("<h2>Главная</h2>")


class RecordsViewSet(GenericViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer

    @extend_schema(parameters=[RecordInputSerializer])
    @action(["GET"], False)
    def get_second_task_table(self, request):
        date_a = datetime.strptime(request.GET.get("date_a"), "%Y-%m-%d").date()
        date_b = datetime.strptime(request.GET.get("date_b"), "%Y-%m-%d").date()
        total, ans = get_second_task_data(date_a, date_b)
        return Response({"answer": ans, "total": total})


def second(request):
    date_a = datetime.strptime(request.GET.get("date_a"), "%Y-%m-%d").date()
    date_b = datetime.strptime(request.GET.get("date_b"), "%Y-%m-%d").date()
    total, ans = get_second_task_data(date_a, date_b)
    return render(request, "second.html", context={"answer": ans, "total": total})


def third(request):
    return render(request, "third.html")


def third_post(request):
    subject = request.POST.get("subject")
    message = request.POST.get("message")
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        request.POST.get("recipient"),
    ]
    mail = Mails.objects.create(
        subject=subject, message=message, recipient=recipient_list[0]
    )
    send_mail(subject, message, email_from, recipient_list)
    mail.is_sent = True
    mail.save()
    return HttpResponse(200)
