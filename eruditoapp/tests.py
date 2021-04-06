from django.test import TestCase
from eruditoapp.models import Subject, Thread, Comment, User, UserProfile
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
# Create your tests here.
def add_subject(name):
    s = Subject.objects.get_or_create(name=name)[0]
    s.save()
    return s
def add_thread(subject, title, body, user, score=0, date=timezone.now()):
    t = Thread.objects.get_or_create(subject=subject, title=title, date=date, user= user, body=body, score=score)[0]
    t.save()
    return t
def add_user(username, password, role='Student', score=0):
    user= User.objects.create_user(username=username, password=password)
    userprof= UserProfile.objects.create(user=user, role=role, score=score, picture= "Default.jpg")
    user.save()
    userprof.save()
    return user

def add_comment(thread, body, user, score=0, date=timezone.now()):
    c= Comment.objects.get_or_create(thread=thread, body=body, date=date, user=user)[0]
    c.score= score
    c.save()
    return c

def basic_population():
    user= add_user("johnny", "123456")
    sub= add_subject("Maths")
    add_subject("Biology")
    add_subject("Physics")
    thr= add_thread(sub, "ThreadTitle", "help me understand", user, score=10)
    add_thread(sub, "secondThread", "seconddatethread", user, score=3, date=datetime(2021,4,3, tzinfo= timezone.utc))
    comm = add_comment(thr, "no idea", user, score=5)
    return user,sub,thr,comm

class HomeViewTests(TestCase):
    
    def test_home_subject_display(self):
        add_subject("Maths")
        add_subject("Biology")
        add_subject("Physics")
        response= self.client.get(reverse('eruditoapp:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maths")
        self.assertContains(response, "Biology")
        self.assertContains(response, "Physics")
        
        num_sub= len(response.context['subjects'])
        self.assertEqual(num_sub, 3)
    
    
class SubjectViewTests(TestCase):
    
    
    def test_subject_thread_display(self):
        user,sub,thr,comm = basic_population()
        response= self.client.get(reverse('eruditoapp:show_subject', args=(sub.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ThreadTitle")
        self.assertContains(response, "help me understand")
    
    def test_sorting_date(self):
        user,sub,thr,comm = basic_population()
        response= self.client.get(reverse('eruditoapp:show_subject', kwargs= {'subject_name_slug': sub.slug, 'sort': "-date",}))
        self.assertEqual(response.status_code, 200)
        self.assertGreater(response.context['threads'][0].date, response.context['threads'][1].date)
    
    def test_sorting_score(self):
        user,sub,thr,comm = basic_population()
        response= self.client.get(reverse('eruditoapp:show_subject', kwargs= {'subject_name_slug': sub.slug, 'sort': "-score",}))
        self.assertEqual(response.status_code, 200)
        self.assertGreater(response.context['threads'][0].score, response.context['threads'][1].score)
    
    def test_thread_search(self):
        user,sub,thr,comm = basic_population()
        response= self.client.get("/subject/maths/search/",{'search': "title"}) #hardcoded URL but reverse becomes tedious function when combining GET request arguments and view funciton parameters 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['threads'][0].title, "ThreadTitle")
        self.assertEqual(len(response.context['threads']),1)

class ThreadViewTests(TestCase):
    
    def test_thread_display(self):
        user,sub,thr,comm = basic_population()
        response= self.client.get(reverse('eruditoapp:show_thread', args=(sub.slug, thr.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "no idea")
        self.assertContains(response, user.username)

class UserProfileViewTests(TestCase):
    def test_profile_display(self):
        user,sub,thr,comm = basic_population()
        userprof= UserProfile.objects.get(user=user)
        response= self.client.get(reverse('eruditoapp:user', args=(user,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, userprof.score)
        self.assertContains(response, user.username)
        self.assertContains(response, thr.title)


                            


    
                                  
