# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:20:32 2021

@author: mic5r
"""
from django.urls import path
from eruditoapp import views

app_name= 'eruditoapp'
urlpatterns= [path('about/', views.about, name='about'),
              path('', views.home, name="home"),
              path('subject/<slug:subject_name_slug>/', views.show_subject,
                   name= 'show_subject'),
              path("subject/<slug:subject_name_slug>/add_thread/", views.add_thread, name="add_thread"),
              path('register/', views.register, name='register'),
              path('login/', views.user_login, name='login'),
              path('restricted/', views.restricted, name='restricted'),
              path('logout/', views.user_logout, name='logout'),
              # path('home/', views.home, name='home'),

              ]
