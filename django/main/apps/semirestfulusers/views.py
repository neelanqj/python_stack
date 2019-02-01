# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User
 
# Create your views here.
def index(request):
	all_users = list(User.objects.all())
	for user in all_users:
		print user.first_name
	content = {
		'users': all_users
	}
	
	return render(request, "semirestfulusers/index.html", content)

def updateRender(request, user):
	userObj = User.objects.get(id=user)
	content = {
		'first_name': userObj.first_name,
		'last_name': userObj.last_name,
		'email_address': userObj.email_address,
		'created_at': userObj.created_at,
		'id': userObj.id
	}
	return render(request, "semirestfulusers/update.html", content)

def update(request, user):
	userObj = User.objects.get(id=user)
	
	userObj.first_name = request.POST['first_name']
	userObj.last_name = request.POST['last_name']
	userObj.email_address = request.POST['email_address']
	
	userObj.save()
	
	return redirect('/users/'+request.POST['id'])

def createRender(request):
	return render(request, "semirestfulusers/create.html")
	
def create(request):
	User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email_address=request.POST['email_address'])
	return redirect('/')
	
def destroy(request, user):
	User.objects.filter(id=user).delete()
	
	return redirect('/')
	
def read(request, user):
	userObj = User.objects.get(id=user)
	content = {
		'first_name': userObj.first_name,
		'last_name': userObj.last_name,
		'email_address': userObj.email_address,
		'created_at': userObj.created_at,
		'id': userObj.id
	}
	return render(request, "semirestfulusers/read.html", content)