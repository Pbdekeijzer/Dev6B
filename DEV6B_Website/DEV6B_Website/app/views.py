"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.template import RequestContext
from datetime import datetime
from .models import DataBaseUser, Users, Jobs
import json 
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.contrib.auth import authenticate, login

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def users(request):
    if request.method == 'GET':

        #different syntax for SELECT * FROM Users
        users = Users.objects.all()

        return_dict = {}

        index = 0

        #add all users to a dictionary, which gets returned at the end
        for i in users:
            return_dict[index] = {"username" : i.username.username, "cash" : i.cash, "experience" : i.experience}
            index = index + 1

        return JsonResponse(return_dict)
    return [], 400

def jobs(request):
    if request.method == 'GET':
        #default user_level
        user_level = 100

        #returns a dictionary with the values from the SELECT * FROM JOBS query
        jobs = Jobs.objects.all()
        
        #The ajax get request sends a dictionary with a username to the backend. The view tries to find the username in the database, else user = None
        dbusername = request.GET.get('username', '')
        try:
            user = Users.objects.get(username=dbusername)
            #enable when actual experience is fixed
            ######user_level = user.experience / 100
        except Users.DoesNotExist:
            user = None
        
        #test
        print(user)

        return_dict = {}

        #to create new keys in the dictionary we need to iterate through a number (index becomes the key for every new entry)
        index = 0

        for i in jobs:
            if i.level_requirement <= user_level:  
                
                #return_dict.setdefault(index, []).append(i.jobname)
                #return_dict.setdefault(index, []).append(i.description)
                #return_dict.setdefault(index, []).append(i.expreward)
                #return_dict.setdefault(index, []).append(i.level_requirement)
                return_dict[index] = {"jobname": i.jobname, "description": i.description, "expreward": i.expreward, "level_requirement": i.level_requirement, "tasks": i.tasks }
                index = index + 1

        #does nothing
        #return_dict = json.dumps(list(jobs))
            
        return JsonResponse(return_dict)
    return [], 400

def test(request):
    return "lol"

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def tester(request):
    if request.method == 'POST':
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('password')

        response_data = {}

        if DataBaseUser.objects.filter(username=loginusername).filter(password=loginpassword):
            response_data['result'] = 'Pass'
        else:
            response_data['result'] = 'Fail'

        return HttpResponse(json.dumps(response_data),
                            content_type="application/json")
    return [], 400

def register(request):
    if request.method == 'POST':
        dbusername = request.POST.get('username')
        dbpassword = request.POST.get('password')
        response_data = {}

        dbuser = DataBaseUser(username=dbusername, password=dbpassword)
        dbuser.save()

        user = Users(username=dbuser, cash=0, experience=0)
        user.save()

        response_data['result'] = 'Create post successful!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        """Renders the contact page."""
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/contact.html',
            {
                'title':'Contact',
                'message':'Your contact page.',
                'year':datetime.now().year,
            }
        )
    #    # Redirect to a success page.
    #    ...
    #else:
    #    # Return an 'invalid login' error message.
    #    ...

def logout_view(request):
    logout(request)

def login_view(request):
    login(request)





    #if request.method == 'POST':
    #    form = DatabaseUserForm(request.POST)
    #    response_data = {}

    #    dbusername = request.form['fname']
    #    dbpassword = request.form['lname']
    #    user = DataBaseUser(username=dbusername, dbpassword=dbpassword)
    #    user.save()

    #    response_data['result'] = "POSTED SUCCESFULLY"
    #    response_data['user'] = dbusername

    #    return HTTPResponse(
    #        json.dumps(response_data), content_type="application/json")
    #else:
    #    return HttpResponse(
    #        json.dumps({"nothing to see": "this isn't happening"}),
    #        content_type="application/json"
    #    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Game',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
