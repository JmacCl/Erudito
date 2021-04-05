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
from eruditoapp.models import Subject, Thread, Comment, UserProfile, User, UsefulResource
import datetime

def populate_erudito():
    maths_thread_comments= [{"body": "u is used as one of the parts you want to substitute, and usually a polynomial expression is an ideal choice for u.",
                             'date':datetime.datetime.now(), 'user': "peter21", 'score':4},
                            {"body": "You should try to use a polynomial expression for u, as this usually simplifies the integral.",
                             'date':datetime.datetime.now(), 'user': 'henryT','score':7}]
    maths_thread_comments_1 = [{"body": "im also unsure some of my teachers are saying they are cancelled others are saying they are going ahead, its driving me crazy !!! :S", 'date':datetime.datetime.now(),
    'user': 'peter21','score':18},{"body": "The exams are cancelled there will be in class tests, best to ask your teacher when these are! :)", 'date':datetime.datetime.now(),
    'user': 'henryT', 'score':25}]

    physics_thread_comments = [{"body":"Yes i absolutely love phsyics i dont really understand it but stem is always fun","date":datetime.datetime.now(),'user':"john5",'score':15},
    {"body":"also phsyics is one of the best sciences","date":datetime.datetime.now(),'user':"john5",'score':1}]

    biology_threads_comment = [{"body":"Both are great choices how ever in my opinion glasgow is the ovbious choice",'date':datetime.datetime.now(),'user':"henryT",'score':12}]

    english_thread_comments = [{"body":"id reccomend looking at the useful resouces its got some links to some really good sites", "date":datetime.datetime.now(),'user':"john5", 'score':12}]

    maths_threads= [{'title':'How do I do integration by parts?',
                     'body':"I don't understand the substitution of u, can somebody help me?",
                    'date': datetime.datetime.now(),
                    'comments': maths_thread_comments, 'score': 15},
                    {'title':'When is the sqa higher exam and when is a good time to start studying?',
                    'body':"im confused on when the exam is can anyone help me?",
                    'date': datetime.datetime.now(),
                    'comments': maths_thread_comments_1, 'score': 6},
                    ]
    physics_threads= [{'title':' Why is a photon "massless" ?',
                     'body':"",
                    'date': datetime.datetime(2021, 4, 3), 'user':'peter21'},
                    {'title':' Is physics a fun subject',
                                     'body':"Im interested in space and im wondering if people would advise if i should take physics or not?",
                                    'date': datetime.datetime(2020, 8, 12), 'user':'henryT','comments':physics_thread_comments}]
    history_threads= [{'title':'Why did WW1 start?',
                     'body':"Apart from the assassination of Archduke Franz Ferdinand, what were other reasons for the start of WWI?",
                    'date': datetime.datetime.now(), 'user':'john5'}]
    english_threads= [{'title':'How do I analyze a poem?',
                     'body':"i have a test tomorrow and im really stuck on this one topic :s",
                    'date': datetime.datetime.now(), 'comments':english_thread_comments}]
    biology_threads= [{'title':'What is the function of the pituitary gland?',
                     'body':"I know it has something to do with hormone regulation, but I'm not quite sure what that means,",
                    'date': datetime.datetime.now()},{'title':"UCAS options help!",
                    'body':"what uni is better for biology im trying to pick me ucas options but im stuck between glasgow and strathclyde",
                    'date':datetime.datetime.now(),
                    'score':32,
                    'comments':biology_threads_comment,
                    'user':"henryT"}]

    subjects= {'Maths': {'threads': maths_threads},
               'Physics':{'threads': physics_threads},
               'History':{'threads': history_threads},
               'English Literature':{'threads': english_threads},
               'Biology':{'threads': biology_threads}}

    users= {'john5': {'password': 'johndoe55'},
            'peter21': {'password':'learning21'},
            'henryT': {'password':'abcdefgh','role':'Teacher'}}



    useful_resources = [{'body':"Mathway",'subject':"Maths",'url':"https://www.mathway.com/"},
    {'body':"BBC BiteSize",'subject':"Maths",'url':"https://www.bbc.co.uk/bitesize/subjects/z6vg9j6"},
    {'body':"Khan academy",'subject':"Maths",'url':"https://www.khanacademy.org/math"},
    {'body':"Corbett Maths",'subject':"Maths",'url':"https://www.youtube.com/user/corbettmaths"},
    {'body':"Biology Crash Course",'subject':"Biology",'url':"https://www.youtube.com/watch?v=QnQe0xW_JY4&list=PL3EED4C1D684D3ADF"},
    {'body':"BBC BiteSize",'subject':"Biology",'url':"https://www.bbc.co.uk/bitesize/subjects/z2svr82"},
    {'body':"Royal Society of Bio",'subject':"Biology",'url':"https://www.rsb.org.uk/"},
    {'body':"BBC BiteSize",'subject':"English Literature",'url':"https://www.bbc.co.uk/bitesize/subjects/zt3rkqt"},
    {'body':"Sparknotes",'subject':"English Literature",'url':"https://www.sparknotes.com/lit/"},
    {'body':"BBC BiteSize",'subject':"Physics",'url':"https://www.bbc.co.uk/bitesize/subjects/zxyb4wx"},
    {'body':"Khan Academy",'subject':"Physics",'url':"https://www.khanacademy.org/science/physics"},
    {'body':"Physics World",'subject':"Physics",'url':"https://physicsworld.com/"},
    {'body':"School History",'subject':"History",'url':"https://schoolhistory.co.uk/"},
    {'body':"BBC BiteSize",'subject':"History",'url':"https://www.bbc.co.uk/bitesize/subjects/z7svr82"}]
    for us,user_data in users.items():
        if ('role' in user_data.keys()):
            u= add_user(username=us, password=user_data['password'],role=user_data['role'])
        else:
            u= add_user(username=us,password=user_data['password']) #password=user_data['password']

    for sub,sub_data in subjects.items():
        u= User.objects.get(username='john5')
        s= add_subject(sub)
        for thr in sub_data['threads']:
            if 'score' in thr.keys():
                score = thr['score']
            else:
                score = 0
            t= add_thread(subject=s, title= thr['title'], body= thr['body'], date=thr['date'], user=u, score=score)
            if 'comments' in thr.keys():
                for comm in thr['comments']:
                    u = User.objects.get(username= comm['user'])
                    if 'score' in comm.keys():
                        score = comm['score']
                    else:
                        score = 0
                    print(comm)
                    print(thr)
                    print(u)
                    add_comment(thread=t, body= comm['body'], date= comm['date'], user=u, score=score)

    for x in useful_resources:
        s = Subject.objects.get(name=x['subject'])
        add_usefulresource(subject = s,body= x['body'], url= x['url'])








def add_subject(name):
    s = Subject.objects.get_or_create(name=name)[0]
    s.save()
    return s

def add_thread(subject, title, body,date, user, score):
    t = Thread.objects.get_or_create(subject=subject, title=title, date=date, user= user, body=body)[0]
    t.score= score
    t.save()
    return t
def add_comment(thread, body, date, user, score):
    c= Comment.objects.get_or_create(thread=thread, body=body, date=date, user=user)[0]
    c.score= score
    c.save()
    return c

def add_user(username, password, role='Student', score=0):
    user= User.objects.create_user(username=username, password=password)
    userprof= UserProfile.objects.create(user=user, role=role, score=score, picture= "Default.jpg")
    user.save()
    userprof.save()
    return user

def add_usefulresource(subject,body,url):
    r= UsefulResource.objects.get_or_create(subject = subject, body=body, url=url)[0]
    r.save()
    return r


if __name__ == '__main__':
    print('Starting erudito population script...')
    populate_erudito()
