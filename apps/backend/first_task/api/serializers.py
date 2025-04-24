from first_task.models import Records
from rest_framework import serializers


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = "__all__"
