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
              path('subject/', views.subjects, name="subjects"),
              path('subject/<slug:subject_name_slug>/', views.show_subject,
                   name= 'show_subject'),
              path("subject/<slug:subject_name_slug>/add_thread/", views.add_thread, name="add_thread"),
              path("subject/<slug:subject_name_slug>/thread/<slug:thread_name_slug>",
                   views.show_thread, name="show_thread"),
              path('register/', views.register, name='register'),
              path('login/', views.user_login, name='login'),
              path('restricted/', views.restricted, name='restricted'),
              path('logout/', views.user_logout, name='logout'),
              path('my-account/', views.my_account, name='my_account'),
              path('register/', views.register, name='register'),
              path('my-account/edit', views.edit_profile, name='edit'),
               path("subject/<slug:subject_name_slug>/thread/<slug:thread_name_slug>/add_comment",
                   views.add_comment, name="add_comment"),

              # path('home/', views.home, name='home'),
               #Below is the url map for comment likes
               path('like_comment/', views.LikeCommentView.as_view(), name = 'like_comment'),
               path('user/<slug:user_name_slug>/', views.show_user,
                    name= 'user'),
                path('my-account/password', views.change_password, name='password'),


              ]
