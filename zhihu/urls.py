# -*- coding: utf-8 -*-
"""
# Created on  2017-04-21 01:39:52

# Author  : homerX
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_daily', views.get_daily, name='get_daily'),
    url(r'^get_(?P<type>day|month|reco)', views.get_hot, name='get_hot'),
    url(r'^get_content', views.get_content, name='get_content'),
    url(r'^get_article', views.get_article, name='get_article'),
]