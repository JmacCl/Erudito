from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from eruditoapp.models import Subject, Thread, Comment, User
from eruditoapp.forms import SubjectForm, ThreadForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.


def about(request):
    context_dict= {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    return render(request, 'erudito/about.html', context=context_dict)

def home(request):

    # most_viewed_threads= Thread.objects.order_by('-views')[:5]
    # context_dict= {}

    # context_dict['threads'] = most_viewed_threads

    context_dict= {}
    visitor_cookie_handler(request)
    subject_list= Subject.objects.all()
    context_dict['subjects']= subject_list
    context_dict['visits'] = request.session['visits']
    return render(request, 'erudito/home.html', context=context_dict)

def subjects(request):
    context_dict= {}
    subject_list= Subject.objects.all()
    context_dict['subjects']= subject_list
    return render(request, 'erudito/subjects.html', context= context_dict)

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request,'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit']= str(datetime.now())
    else:
        request.session['last_visit']= last_visit_cookie

    request.session['visits']= visits

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def show_subject(request, subject_name_slug):
    context_dict={}
    try:
        subject= Subject.objects.get(slug=subject_name_slug)
        threads= Thread.objects.filter(subject=subject).order_by('-score') #unchecked if works or not, could test after break by creating more in population script
        context_dict['threads']= threads
        context_dict['subject']= subject
    except Subject.DoesNotExist:
        context_dict['threads']= None
        context_dict['subject']= None
    return render(request, 'erudito/subject.html', context=context_dict)

def show_thread(request, subject_name_slug, thread_name_slug):
    context_dict={}
    try:
        subject= Subject.objects.get(slug=subject_name_slug)
        thread= Thread.objects.get(slug=thread_name_slug)
        comments= Comment.objects.filter(thread=thread)
        context_dict['subject']= subject
        context_dict['thread']= thread
        context_dict['comments']= comments
    except Thread.DoesNotExist:
        context_dict['thread']= None
        context_dict['comments']= None
    return render(request, 'erudito/thread.html', context= context_dict)

@login_required
def add_thread(request, subject_name_slug):
    try:
        subject= Subject.objects.get(slug=subject_name_slug)
    except Subject.DoesNotExist:
        subject= None
    try:
        user= request.user
    except User.DoesNotExist:
        user= None

    if subject is None:
        return redirect('/')
    if user is None:
        return redirect('/')

    form= ThreadForm()
    if request.method=="POST":
        form= ThreadForm(request.POST)
        if form.is_valid():
            if subject:
                thread= form.save(commit=False)
                thread.subject = subject
                thread.score= 0
                thread.user= user
                thread.save()
                return redirect(reverse('eruditoapp:show_subject', kwargs={'subject_name_slug':
                                                                       subject_name_slug}))

            else:
                print(form.errors)
    context_dict= {'form':form, 'subject': subject}
    return render(request, 'erudito/add_thread.html', context=context_dict)

def register(request):
    registered= False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form= UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user= user

            if 'picture' in request.FILES:
                profile.picture= request.FILES['picture']
            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form= UserProfileForm()

    return render(request, 'erudito/register.html', context= {'user_form': user_form,
                                                            'profile_form': profile_form,
                                                            'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('eruditoapp:about'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'erudito/login.html')


@login_required
def my_account(request):
    return render(request, 'erudito/my_account.html')

@login_required
def restricted(request):
    return render(request, 'erudito/restricted.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('eruditoapp:about'))
