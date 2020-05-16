'''
Go big or go home!
author: WangQuanyi
date: 2020-05-15 14:32
name: urls.py
contact: wang0759@algonquinlive.com

'''
from django.urls import path
# from current directory import function views
from . import views

# list the urls
urlpatterns = [
    path("", views.index),
    path("second", views.second)
]
