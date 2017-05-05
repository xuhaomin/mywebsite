from django.shortcuts import render
from django.http import HttpResponse
import re
import json
from video.models import Video
from django.db.models import Q

from .parser.youku import *


def get_video(request):
    return render(request, 'get_video.html')


def parse_website(request):
    url = request.GET.get('url', '')
    id_pattern = re.compile(r'(?:id_)*(\w{13,15})(?:==)*')
    vid = re.findall(id_pattern, url)
    result = {}
    if not vid:
        result['vid'] = 'no vid found'
    else:
        result['vid'] = vid[0]
        img = Video.objects.get(vid=vid[0]).img
        result['img'] = img
        urls = get_mp4_urls_from_vid(vid[0])
        if urls:
            result['video_urls'] = urls
    return HttpResponse(json.dumps(result))


def search_video_by_title(request):
    title = request.GET.get('title', '')
    if title:
        keys = re.split(";|,|\*|\s", title)
    else:
        keys = []
    page = int(request.GET.get('page', 1))
    res = Video.objects
    result = {}
    for key in keys:
        res = res.filter(
            Q(title__icontains=key) | Q(series__icontains=key))
    res = res.order_by('title')
    counts = res.count()
    result['total_count'] = counts
    left = (page - 1) * 30
    right = page * 30
    if left <= counts:
        if right > counts:
            items = list(res.values('title', 'img', 'vid')[left:counts + 1])
        else:
            items = list(res.values('title', 'img', 'vid')[left:right])
    else:
        items = []
    for ele in items:
        if ele['img'].startswith('//'):
            ele['img'] = 'http:' + ele['img']
        ele['id'] = ele['vid']
    result['items'] = items
    return HttpResponse(json.dumps(result))
