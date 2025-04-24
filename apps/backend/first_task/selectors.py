from datetime import timedelta

from first_task.models import Records


def get_second_task_data(date_a, date_b):
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
        ans.append(
            [
                date,
                t1[i].record,
                t2[i].record,
                t3[i],
                m1[i].record,
                m2[i].record,
                m3[i],
                q[i].record,
                "24",
            ]
        )
        hours.append(24)

    def sum_of(query):
        a = 0
        for i in query:
            a += i.record
        return a

    total = [
        "Итого",
        sum_of(t1) / len(t1),
        sum_of(t2) / len(t1),
        sum(t3) / len(t1),
        sum_of(m1),
        sum_of(m2),
        sum(m3),
        sum_of(q),
        sum(hours),
    ]
    return total, ans
