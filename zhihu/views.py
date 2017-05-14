from django.http import HttpResponse
import json
from zhihu.models import Daily, Explore, Article
import re

count = 6


def get_daily(request):
    offset = int(request.GET.get('offset', 0))
    get_count = count + offset
    daily = Daily.objects.order_by('-update_time')[offset:get_count].values('title', 'id', 'img')
    response = HttpResponse(json.dumps(list(daily)))
    return response


def get_hot(request, type='day'):
    offset = int(request.GET.get('offset', 0))
    get_count = count + offset
    hot = Explore.objects
    if type == 'day':
        hot = hot.filter(day__isnull=False)
    if type == 'month':
        hot = hot.filter(month__isnull=False)
    if type == 'reco':
        hot = hot.filter(reco__isnull=False)
    data = hot.order_by(
        '-update_time')[offset:get_count].values('title', 'aid', 'qid', 'abstract', 'author')
    response = HttpResponse(json.dumps(list(data)))
    return response


def get_article(request):
    offset = int(request.GET.get('offset', 0))
    get_count = count + offset
    data = hot.order_by(
        '-update_time')[offset:get_count].values('title', 'id', 'abstract', 'author')
    response = HttpResponse(json.dumps(list(data)))
    return response


def get_content(request):
    aid = request.GET.get('aid')
    content = Explore.objects.get(aid=aid)
    data = {
        'title': content.title,
        'content': re.sub(r'width="\d+"', 'width=92%', content.full_content),
        'author': content.author
    }
    response = HttpResponse(json.dumps(data))
    return response
