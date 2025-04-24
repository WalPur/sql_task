from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from first_task.api.serializers import (
    EmailInputSerializer,
    EmailSerializer,
    OneEmailInputSerializer,
    RecordInputSerializer,
    RecordsSerializer,
)
from first_task.models import Mails, Records
from first_task.selectors import get_second_task_data
from first_task.services import send_emails
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class RecordsViewSet(GenericViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer

    @extend_schema(parameters=[RecordInputSerializer])
    @action(["GET"], False)
    def get_second_task_table(self, request):
        """Получение данных в JSON таблицы показателей"""
        date_a = datetime.strptime(request.GET.get("date_a"), "%Y-%m-%d").date()
        date_b = datetime.strptime(request.GET.get("date_b"), "%Y-%m-%d").date()
        total, ans = get_second_task_data(date_a, date_b)
        return Response({"answer": ans, "total": total})


class EmailViewSet(GenericViewSet, ListModelMixin):
    queryset = Mails.objects.all()
    serializer_class = EmailSerializer

    @action(["POST"], False, serializer_class=EmailInputSerializer)
    def input_emails(self, request):
        """Отправка письма множеству адресов"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.validated_data["subject"]
        message = serializer.validated_data["message"]
        recipient_list = serializer.validated_data["recipients"]
        status = send_emails(subject, message, recipient_list)
        return Response(status)

    @action(["POST"], False, serializer_class=OneEmailInputSerializer)
    def input_email(self, request):
        """Отправка письма одному адресу"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.validated_data["subject"]
        message = serializer.validated_data["message"]
        recipient = serializer.validated_data["recipient"]
        status = send_emails(subject, message, [recipient])
        return Response(status)


def second(request):
    """Отображение таблицы показателей"""
    date_a = datetime.strptime(request.GET.get("date_a"), "%Y-%m-%d").date()
    date_b = datetime.strptime(request.GET.get("date_b"), "%Y-%m-%d").date()
    total, ans = get_second_task_data(date_a, date_b)
    return render(request, "second.html", context={"answer": ans, "total": total})


def third(request):
    """Форма для отправки письма"""
    return render(request, "third.html")
