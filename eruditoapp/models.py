from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
    body= models.CharField(max_length=BODY_MAX_LENGTH)
    score= models.IntegerField(default=0) #called score in ER diagram
    date= models.DateTimeField()

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    BODY_MAX_LENGTH= 10000
    thread= models.ForeignKey(Subject, on_delete= models.CASCADE)
    body= models.CharField(max_length= BODY_MAX_LENGTH)
    score= models.IntegerField(default=0)
    date= models.DateTimeField()
    
    def __str__(self):
        return self.body[:25] #returns first 25 characters of string
    

class UserProfile(models.Model):
    MAX_LENGTH= 64
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    picture= models.ImageField(upload_to='profile_images', blank=True)
    fullname=models.CharField(max_length= MAX_LENGTH)
    email= models.EmailField()
    score= models.IntegerField()
    role= models.CharField(max_length= MAX_LENGTH)

    def __str__(self):
        return self.user.username
