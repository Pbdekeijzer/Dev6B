"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from .models import DataBaseUser, Users, Jobs
import json 
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError

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

def jobs(request):
    if request.method == 'GET':
        #default user_level
        user_level = 1

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
                return_dict[index] = {"jobname": i.jobname, "description": i.description, "expreward": i.expreward, "level_requirement": i.level_requirement }
                index = index + 1

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

def users(request):
    return HTTPResponse("EMPTY")

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
