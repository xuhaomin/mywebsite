# -*- coding: utf-8 -*-
"""
# Created on  2017-04-21 01:39:52

# Author  : homerX
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^citylist/', views.get_citylist, name='get_citylist'),
    url(r'^cities/', views.cities, name='cities'),
    url(r'^catagorylist/', views.get_catagorylist, name='get_catagorylist'),
    url(r'^position/', views.get_position, name='get_position'),
]