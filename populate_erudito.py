# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:06:34 2021

@author: mic5r
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'erudito.settings')
import django
django.setup()
from eruditoapp.models import Subject, Thread, Comment, UserProfile, User
import datetime

def populate_erudito():
    maths_thread_comments= [{"body": "u is used as one of the parts you want to substitute, and usually a polynomial expression is an ideal choice for u.",
                             'date':datetime.datetime.now()}]
    maths_threads= [{'title':'How do I do integration by parts?',
                     'body':"I don't understand the substitution of u, can somebody help me?",
                    'date': datetime.datetime.now(),
                    'comments': maths_thread_comments}]
    physics_threads= [{'title':' Why is a photon "massless" ?',
                     'body':"",
                    'date': datetime.datetime(2013, 7, 29)}]
    history_threads= [{'title':'Why did WW1 start?',
                     'body':"Apart from the assassination of Archduke Franz Ferdinand, what were other reasons for the start of WWI?",
                    'date': datetime.datetime.now()}]
    english_threads= [{'title':'How do I analyze a poem?',
                     'body':"",
                    'date': datetime.datetime.now()}]
    biology_threads= [{'title':'What is the function of the pituitary gland?',
                     'body':"I know it has something to do with hormone regulation, but I'm not quite sure what that means,",
                    'date': datetime.datetime.now()}]

    subjects= {'Maths': {'threads': maths_threads},
               'Physics':{'threads': physics_threads},
               'History':{'threads': history_threads},
               'English Literature':{'threads': english_threads},
               'Biology':{'threads': biology_threads}}

    users= {'john5': {'password': 'johndoe55'},
            'peter21': {'password':'learning21'},
            'henryT': {'password':'abcdefgh','role':'Teacher'}}
    for us,user_data in users.items():
        if ('role' in user_data.keys()):
            u= add_user(username=us, password=user_data['password'],role=user_data['role'])
        else:
            u= add_user(username=us,password=user_data['password']) #password=user_data['password']

    for sub,sub_data in subjects.items():
        u= User.objects.get(username='john5')
        s= add_subject(sub)
        for thr in sub_data['threads']:
            t= add_thread(subject=s, title= thr['title'], body= thr['body'], date=thr['date'], user=u)
            if 'comments' in thr.keys():
                for comm in thr['comments']:
                    print(comm)
                    print(thr)
                    print(u)
                    add_comment(thread=t, body= comm['body'], date= comm['date'], user=u)





def add_subject(name):
    s = Subject.objects.get_or_create(name=name)[0]
    s.save()
    return s

def add_thread(subject, title, body,date, user, score=0):
    t = Thread.objects.get_or_create(subject=subject, title=title, date=date, user= user, body=body)[0]
    t.score= score
    t.save()
    return t
def add_comment(thread, body, date, user, score=0):
    c= Comment.objects.get_or_create(thread=thread, body=body, date=date, user=user)[0]
    c.score= score
    c.save()
    return c

def add_user(username, password, role='Student', score=0):
    user= User.objects.create_user(username=username, password=password)
    #user= UserProfile.objects.get_or_create(user_id=username, role=role)
    #user.score= score
    user.save()
    return user


if __name__ == '__main__':
    print('Starting erudito population script...')
    populate_erudito()
