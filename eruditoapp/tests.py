from django.test import TestCase
from eruditoapp.models import Subject, Thread, Comment, User, UserProfile
from django.urls import reverse
from django.utils import timezone
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
        user= add_user("johnny", "123456")
        sub= add_subject("Maths")
        add_subject("Biology")
        add_subject("Physics")
        add_thread(sub, "ThreadTitle", "help me understand", user, score=10)
        response= self.client.get(reverse('eruditoapp:show_subject', args=(sub.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ThreadTitle")
        self.assertContains(response, "help me understand")
        

                                  
        
