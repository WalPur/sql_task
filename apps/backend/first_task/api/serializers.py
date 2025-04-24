from calendar import c

from first_task.models import Records
from rest_framework import serializers


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = "__all__"


class RecordInputSerializer(serializers.Serializer):
    date_a = serializers.DateField()
    date_b = serializers.DateField()
