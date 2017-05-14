# -*- coding: utf-8 -*-
"""
# Created on  2017-04-21 01:39:52

# Author  : homerX
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_day', views.get_day, name='get_day'),
    url(r'^get_week', views.get_week, name='get_week'),
]