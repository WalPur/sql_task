from django.db import models


class Record_names(models.Model):
    counter_id = models.IntegerField()
    record_name = models.CharField(max_length=50)
    is_calculated_diff = models.BooleanField()
    record_names_rus = models.CharField(max_length=255)


class Records(models.Model):
    counter_id = models.IntegerField()
    record_name_id = models.ForeignKey("Record_names", on_delete=models.CASCADE)
    date_record = models.DateField(auto_now=False)
    record = models.FloatField()
    record_diff = models.FloatField()
    period = models.IntegerField()
