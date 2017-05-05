from django.shortcuts import render
from django.http import HttpResponse
import json
from lagou.models import Position
from django.db import connection
import random


def get_citylist(request):
    cur = connection.cursor()
    cur.execute(
        'select city,count(*) from lagou_position group by city order by count(*) DESC')
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
        'select city,count(*) from lagou_position group by city order by count(*) DESC')
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
    if city:
        p = p.filter(city__exact=city)
    if catagory:
        p = p.filter(catagory__exact=catagory)
    count = len(p.values().all())
    resp = []
    ind_col = []
    if count < 10:
        resp = list(p.values('position', 'city', 'salary',
                             'company', 'requirement').all())
    else:
        for i in range(10):
            ind = random.randint(0, count - 1)
            ind_col.append(ind)
        for i in set(ind_col):
            data = p.values(
                'position', 'city', 'salary', 'company', 'requirement').all()[i]
            resp.append(data)
    resp.sort(key=lambda x: len(x['requirement']))
    response = HttpResponse(json.dumps(resp))
    return response
