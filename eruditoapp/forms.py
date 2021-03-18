# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:09:19 2021
@author: mic5r
"""
from django import forms
from eruditoapp.models import Thread,Subject, UserProfile
from django.contrib.auth.models import User

class SubjectForm(forms.ModelForm):
    name= forms.CharField(max_length=Subject.NAME_MAX_LENGTH, help_text="Please enter the category name.")
    views= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug= forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model= Subject
        fields= ('name',)

class ThreadForm(forms.ModelForm):
    title= forms.CharField(max_length=Thread.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
    url= forms.URLField(max_length=200, help_text="Please enter the URL of the page")
    views= forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    
    class Meta:
        model= Thread
        exclude= ('category',)
    
    def clean(self):
        cleaned_data= self.cleaned_data
        url= cleaned_data.get("url")
        if url and not url.startswith('http://'):
            url= f'http://{url}'
            cleaned_data['url']=url
        return cleaned_data
    
class UserForm(forms.ModelForm):
    password= forms.CharField(widget= forms.PasswordInput())
    class Meta: 
        model=User
        fields=('username', 'email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields= ('website', 'picture')
        
    