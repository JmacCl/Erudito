from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    NAME_MAX_LENGTH=128
    name= models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    # views= models.IntegerField(default=0)
    # likes= models.IntegerField(default=0)
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
    subject= models.ForeignKey(Subject, on_delete= models.CASCADE)
    title= models.CharField(max_length=TITLE_MAX_LENGTH)
    # url= models.URLField()
    views= models.IntegerField(default=0) #not mentioned in ER
    likes= models.IntegerField(default=0) #called score in ER diagram
    date= models.DateTimeField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    picture= models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
