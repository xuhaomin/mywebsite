from django.http import HttpResponse
import json
from liepin.models import Position
from django.db import connection
import random


def get_citylist(request):
    cur = connection.cursor()
    cur.execute(
        'select city,count(*) from liepin_position group by city order by count(*) DESC')
    city_list = list(cur.fetchall())
    resp = []
    search_word = request.GET.get('words', '')
    for city in city_list:
        if search_word in city[0]:
            resp.append({'id': city[0], 'text': city[0]})
    response = HttpResponse(json.dumps(resp))

    return response


def cities(request):
    cur = connection.cursor()
    cur.execute(
        'select city,count(*) from liepin_position group by city order by count(*) DESC')
    city_list = cur.fetchall()
    resp = []
    for city in city_list:
        resp.append({"name": city[0], "count": city[1]})
    response = HttpResponse(json.dumps(resp))

    return response


def get_catagorylist(request):
    catagory_list = list(Position.objects.values_list(
        'catagory', flat=True).distinct())
    return HttpResponse(json.dumps(catagory_list))


def get_position(request):
    city = request.GET.get('city', '')
    catagory = request.GET.get('catagory', '')
    p = Position.objects
    if city and city != '0':
        p = p.filter(city__exact=city)
    if catagory:
        if catagory == 'python':
            p = p.filter(python__isnull=False)
        if catagory == 'data':
            p = p.filter(data__isnull=False)
        if catagory == 'spider':
            p = p.filter(spider__isnull=False)
    count = len(p.values().all())
    resp = []
    ind_col = []
    if count < 10:
        resp = list(p.values('pid', 'position', 'city', 'salary',
                             'company', 'requirement', 'company', 'companylink').all())
    else:
        i = 0
        while i < 9:
            ind = random.randint(0, count - 1)
            if ind not in ind_col:
                ind_col.append(ind)
                i += 1
        for i in set(ind_col):
            data = p.values(
                'pid', 'position', 'city', 'salary', 'company', 'requirement', 'companylink').all()[i]
            resp.append(data)
    resp.sort(key=lambda x: len(x['requirement']))
    response = HttpResponse(json.dumps(resp))
    return response
