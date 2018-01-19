#!/usr/bin/env python3
#coding=utf-8
"""
# Author: huangyisan
# Created Time : 六  5/ 6 17:30:08 2017
# File Name: ../online/urls.py
# Description:

"""
from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'^create/',views.create, name='create'),
    url(r'^save/',views.save, name='save'),
    ]
