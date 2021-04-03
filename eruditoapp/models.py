from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# import uuid

# Create your models here.

class Subject(models.Model):
    NAME_MAX_LENGTH=128
    name= models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug= models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super(Subject, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural= 'Subjects'

    def __str__(self):
        return self.name


class Thread(models.Model):
    TITLE_MAX_LENGTH=128
    BODY_MAX_LENGTH= 10000
    subject= models.ForeignKey(Subject, on_delete= models.CASCADE)
    title= models.CharField(max_length=TITLE_MAX_LENGTH)
    body= models.CharField(max_length=BODY_MAX_LENGTH, default="")
    score= models.IntegerField(default=0) #called score in ER diagram
    date= models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    slug= models.SlugField(unique=True)

    # thread_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    def save(self, *args, **kwargs):
        self.slug= slugify(self.title)
        super(Thread, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    BODY_MAX_LENGTH= 10000
    thread= models.ForeignKey(Thread, on_delete= models.CASCADE)
    body= models.CharField(max_length= BODY_MAX_LENGTH, default="")
    score= models.IntegerField(default=0)
    date= models.DateTimeField(auto_now_add=True)
    # likes = models.IntegerField(default=0)
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.body[:25] #returns first 25 characters of string



class UserProfile(models.Model):
    MAX_LENGTH= 64
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    picture= models.ImageField(upload_to='profile_images', default='Default.jpg', blank=False)
    # fullname=models.CharField(max_length= MAX_LENGTH)
    # email= models.EmailField() provided by Django User as fields

    USER_ROLES=(('teacher',"Teacher"),
        ('student',"Student"))
    role=models.CharField(max_length=10,choices=USER_ROLES,default="student")

    score= models.IntegerField(default=0)


    def __str__(self):
        return self.user.username


# Model for useful resources page
class UsefulResource(models.Model):

    BODY_MAX_LENGTH= 10000
    subject= models.ForeignKey(Subject, on_delete= models.CASCADE)
    body= models.CharField(max_length=BODY_MAX_LENGTH, default="")


    def save(self, *args, **kwargs):
        super(UsefulResource, self).save(*args, **kwargs)

    def __str__(self):
        return self


class Vote(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    comment= models.ManyToManyField(Comment)
    #possibly add a boolean has_voted

    def __str__(self):
        return self.user.username + self.comment.body[:25]


class ThreadVote(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    thread= models.ManyToManyField(Thread)
    def __str__(self):
        return self.user.username + self.thread.body[:25]
