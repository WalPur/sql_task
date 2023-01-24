from django.http import HttpResponse
from django.shortcuts import render
from .models import Record_names, Records
from django.db.models import Avg, Sum
from datetime import datetime, timedelta


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def first(request):
    id = int(request.GET.get("id"))
    date_a = datetime.strptime(request.GET.get("date_a"), "%Y-%m-%d").date()
    date_b = datetime.strptime(request.GET.get("date_b"), "%Y-%m-%d").date()
    record_name = Record_names.objects.get(id=id)
    if record_name.is_calculated_diff:
        records = Records.objects.filter(
            record_name_id_id=id, date_record__gte=date_a, date_record__lte=date_b
        ).aggregate(Sum("record_diff"))["record_diff__sum"]
    elif id in (11, 12):
        records = Records.objects.filter(
            record_name_id_id=id, date_record__gte=date_a, date_record__lte=date_b
        ).aggregate(Avg("record"))["record__avg"]
    else:
        records = Records.objects.filter(
            record_name_id_id=id, date_record__gte=date_a, date_record__lte=date_b
        ).aggregate(Sum("record"))["record__sum"]
    return HttpResponse(
        f"{record_name.record_names_rus} с {date_a} по {date_b} = {records}"
    )


def second(request):
    date_a = datetime.strptime(request.GET.get("date_a"), "%Y-%m-%d").date()
    date_b = datetime.strptime(request.GET.get("date_b"), "%Y-%m-%d").date()
    t1 = Records.objects.filter(
        record_name_id_id=11, date_record__gte=date_a, date_record__lte=date_b
    )
    t2 = Records.objects.filter(
        record_name_id_id=12, date_record__gte=date_a, date_record__lte=date_b
    )
    t3 = []
    for i in range(len(t1)):
        t3.append(t1[i].record - t2[i].record)
    m1 = Records.objects.filter(
        record_name_id_id=2, date_record__gte=date_a, date_record__lte=date_b
    )
    m2 = Records.objects.filter(
        record_name_id_id=3, date_record__gte=date_a, date_record__lte=date_b
    )
    m3 = []
    for i in range(len(m1)):
        m3.append(m1[i].record - m2[i].record)
    q = Records.objects.filter(
        record_name_id_id=1, date_record__gte=date_a, date_record__lte=date_b
    )
    ans = []
    hours = []
    for i in range(len(t1)):
        date = date_a + timedelta(days=i)
        date = date.strftime("%d.%m.%Y")
        ans.append([date, t1[i].record, t2[i].record,
                   t3[i], m1[i].record, m2[i].record, m3[i], q[i].record, '24',])
        hours.append(24)

    def sum_of(query):
        a = 0
        for i in query:
            a += i.record
        return a
    total = [
        'Итого', sum_of(t1) / len(t1), sum_of(t2) / len(t1), sum(t3) / len(t1),
        sum_of(m1), sum_of(m2), sum(m3), sum_of(q), sum(hours),
    ]
    return render(request, 'second.html', context={'answer': ans, 'total': total})
    return HttpResponse(f"{ans}")
