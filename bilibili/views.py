from django.http import HttpResponse
import json
from bilibili.models import Archive, Owner
import time


def get_day(request):
    now = int(time.time())
    t = now - 86400
    return get(t)


def get_week(request):
    now = int(time.time())
    t = now - 86400 * 7
    return get(t)


def get(t):
    archives = Archive.objects.filter(pubdate__gte=t).values()
    data = {}
    for archive in archives:
        if archive['owner_id'] in data:
            data[archive['owner_id']]['archive'].append(archive)
        else:
            mid = archive['owner_id']
            data[mid] = {
                'face': Owner.objects.get(mid=mid).face,
                'name': Owner.objects.get(mid=mid).name,
                'archive': [archive],
                'mid': mid
            }
    res = []
    for v in data:
        res.append(data[v])
    response = HttpResponse(json.dumps(res))
    return response
