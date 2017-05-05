# -*- coding: utf-8 -*-
"""
# Created on  2017-04-12 00:32:09

# Author  : homerX
"""
import base64
import requests
import urllib.parse


def yk_t(s1, s2):
    ls = list(range(256))
    t = 0
    for i in range(256):
        t = (t + ls[i] + my_ord(s1[i % len(s1)])) % 256
        ls[i], ls[t] = ls[t], ls[i]
    s = bytearray()
    x, y = 0, 0
    for i in range(len(s2)):
        y = (y + 1) % 256
        x = (x + ls[y]) % 256
        ls[x], ls[y] = ls[y], ls[x]
        s.append(my_ord(s2[i]) ^ ls[(ls[x] + ls[y]) % 256])
    return bytes(s)


def my_ord(n):
    if type(n) == int:
        return n
    else:
        return ord(n)


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


def get_hd(fm):
    hd_id_dict = {
        '3gp': '0',
        '3gphd': '1',
        'flv': '0',
        'flvhd': '0',
        'mp4': '1',
        'mp4hd': '1',
        'mp4hd2': '1',
        'mp4hd3': '1',
        'hd2': '2',
        'hd3': '3',
    }
    return hd_id_dict[fm]


def get_urls_from_vid(vid):
    vid = vid
    url = 'http://play.youku.com/play/get.json?vid={videoID}&ct=12'.format(
        videoID=vid)
    r = requests.get(url, )
    data = r.json()['data']
    fileid_dict = {}
    for stream in data['stream']:
        if stream.get('channel_type') == 'tail':
            continue
        format1 = stream.get('stream_type')
        fileid = stream['segs'][0]['fileid']
        fileid_dict[format1] = fileid
    sid, token = yk_t(
        b'becaf9be', base64.b64decode(
            data['security']['encrypt_string'].encode('ascii'))
    ).decode('ascii').split('_')

    def get_fileid(format1, n):
        number = hex(int(str(n), 10))[2:].upper()
        if len(number) == 1:
            number = '0' + number
        streamfileids = fileid_dict[format1]
        fileid = streamfileids[0:8] + number + streamfileids[10:]
        return fileid

    # get ep
    def generate_ep(format1, n):
        fileid = get_fileid(format1, n)
        ep_t = yk_t(
            b'bf7e5f01',
            ('%s_%s_%s' % (sid, fileid, token)).encode('ascii')
        )
        ep = base64.b64encode(ep_t).decode('ascii')
        return ep

    sip = data['security']['ip']

    video_urls_dict = {}
    for stream in data['stream']:
        if stream.get('channel_type') == 'tail':
            continue
        stream_type = stream.get('stream_type')
        video_urls = []
        for dt in stream['segs']:
            n = str(stream['segs'].index(dt))
            param = {
                'K': dt['key'],
                'hd': get_hd(stream_type),
                'myp': 0,
                'ypp': 0,
                'ctype': 12,
                'ev': 1,
                'token': token,
                'oip': sip,
                'ep': generate_ep(stream_type, n)
            }
            video_url = \
                'http://k.youku.com/player/getFlvPath/' + \
                'sid/' + sid + \
                '_00' + \
                '/st/' + parse_ext_l(stream_type) + \
                '/fileid/' + get_fileid(stream_type, n) + '?' + \
                urllib.parse.urlencode(param)
            video_urls.append(video_url)
        video_urls_dict[stream_type] = video_urls
    return video_urls_dict


def get_mp4_urls_from_vid(vid):
    stream = {'3gphd': '标清', 'mp4hd': '超清', 'mp4': '高清'}
    video_urls_dict = get_urls_from_vid(vid)
    mp4_urls = [{'mod': key, 'urls': urls, 'text': stream[key]}
                for key, urls in video_urls_dict.items()
                if key in ('3gphd', 'mp4hd', 'mp4')]
    for i, v in enumerate(mp4_urls):
        v['id'] = i+1
    return mp4_urls


if __name__ == '__main__':
    print(get_mp4_urls_from_vid('XMjcwMjAxMTA0NA'))
