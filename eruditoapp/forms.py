# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:09:19 2021
@author: mic5r
"""
from django import forms
from eruditoapp.models import Thread, Subject, UserProfile, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class SubjectForm(forms.ModelForm):
    name= forms.CharField(max_length=Subject.NAME_MAX_LENGTH, help_text="Please enter the category name.")
    views= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug= forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model= Subject
        fields= ('name',)

class ThreadForm(forms.ModelForm):
    title= forms.CharField(max_length=Thread.TITLE_MAX_LENGTH,widget=forms.Textarea(attrs={'style' : 'height: 2em; width: 30em;','class':'input-look'}))
    body= forms.CharField(max_length= Thread.BODY_MAX_LENGTH,widget=forms.Textarea(attrs={'style' : 'height: 10em; width: 30em;','class':'input-look'}))
    # views= forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model= Thread
        fields= ('title', 'body',)

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super(ThreadForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     cleaned_data= self.cleaned_data
    #     url= cleaned_data.get("url")
    #     if url and not url.startswith('http://'):
    #         url= f'http://{url}'
    #         cleaned_data['url']=url
    #     return cleaned_data

class CommentForm(forms.ModelForm):
    body= forms.CharField(max_length=Comment.BODY_MAX_LENGTH, widget=forms.Textarea(attrs={'style' : 'height: 5em; width: 30em;','class':'input-look'}))
    # likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model= Comment
        fields= ('body',)

class UserForm(forms.ModelForm):
    password= forms.CharField(widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields= ('picture','role')

class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
        'email',
        'username',
        )
