from calendar import c

from first_task.models import Mails, Records
from rest_framework import serializers


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = "__all__"


class RecordInputSerializer(serializers.Serializer):
    date_a = serializers.DateField(default="2021-01-01")
    date_b = serializers.DateField(default="2021-05-01")


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mails
        fields = "__all__"


class EmailInputSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipients = serializers.ListField(child=serializers.EmailField())


class OneEmailInputSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient = serializers.EmailField()
