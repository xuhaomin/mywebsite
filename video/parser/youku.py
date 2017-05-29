# -*- coding: utf-8 -*-
"""
# Created on  2017-04-12 00:32:09

# Author  : homerX
"""
import requests
import time
import random
import string
import re


def parse_ext_l(fm):
    ext_dict = {
        '3gp': 'flv',
        '3gphd': 'mp4',
        'flv': 'flv',
        'flvhd': 'flv',
        'mp4': 'mp4',
        'mp4hd': 'mp4',
        'mp4hd2': 'flv',
        'mp4hd3': 'flv',
        'hd2': 'flv',
        'hd3': 'flv',
    }
    return ext_dict[fm]


def get_ysuid():
    return '%d%s' % (int(time.time()), ''.join([
        random.choice(string.ascii_letters) for i in range(3)]))


def get_urls_from_vid(vid):

    r = requests.get('https://log.mmstat.com/eg.js')
    try:
        cna = re.findall(r'Etag="(\S+)"', r.text)[0]
    except:
        return

    basic_data_params = {
        'vid': vid,
        'ccode': '0401',
        'client_ip': '192.168.1.1',
        'client_ts': time.time() / 1000,
        'utid': cna,
    }

    cookies = {
        '__ysuid': get_ysuid(),
        'xreferrer': 'http://www.youku.com',
    }

    # url = 'http://play.youku.com/play/get.json?vid={videoID}&ct=12'.format(
    #    videoID=vid)
    url = 'https://ups.youku.com/ups/get.json'

    r = requests.get(url, params=basic_data_params, cookies=cookies)
    data = r.json()['data']
    video_urls_dict = {}
    for video in data['stream']:
        video_urls_dict[video['stream_type']] = [i['cdn_url'] for i in video['segs']]
    print(video_urls_dict)
    return video_urls_dict


def get_mp4_urls_from_vid(vid):
    stream = {'3gphd': '标清', 'mp4hd': '超清', 'mp4': '高清'}
    video_urls_dict = get_urls_from_vid(vid)
    mp4_urls = [{'mod': key, 'urls': urls, 'text': stream[key]}
                for key, urls in video_urls_dict.items()
                if key in ('3gphd', 'mp4hd', 'mp4')]
    for i, v in enumerate(mp4_urls):
        v['id'] = i + 1
    return mp4_urls


if __name__ == '__main__':
    print(get_mp4_urls_from_vid('XMjcwMjAxMTA0NA'))
