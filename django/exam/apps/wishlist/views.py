# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt, re
from django.shortcuts import redirect, render
from django.contrib import messages

from models import *

# Create your views here.
def index(request):
	return redirect('/main')
	
def gateway(request):
	return render(request, 'wishlist/gateway.html')
	
def login(request):
	print "got here!"
	try:
		user = User.objects.get(name = request.POST['username'])
		hashed_password = user.password
		entered_password = request.POST['password']
		
		if bcrypt.checkpw(entered_password.encode(), hashed_password.encode()):
			request.session['id'] = user.id
			return redirect('/dashboard')
		else:		
			messages.add_message(request, messages.INFO, 'Invalid username or password. Please try again.')
			return redirect('/main')
	except:
			messages.add_message(request, messages.INFO, 'Invalid username or password. Please try again.')
			return redirect('/main')

def logout(request):
	del request.session['id']
	request.session.modified = True
	
	return redirect('/main')
		
def register(request):
	name = request.POST['name']
	username = request.POST['username']
	datehired = request.POST['datehired']
	password = request.POST['password']	
	confirm_password = request.POST['confirm_password']	
	
	errors = 0

	if not re.match(r"^[a-zA-Z]+$", name):
		messages.add_message(request, messages.INFO, "Invalid name.")
		errors += 1
	
	if len(name) < 3:
		messages.add_message(request, messages.INFO, "Name should be larger than 3 characters.")
		errors += 1
		
	if len(username) < 3:
		messages.add_message(request, messages.INFO, "Username should be larger than 3 characters.")
		errors += 1
		
	if password == "":
		messages.add_message(request, messages.INFO, "Password is not allowed to be empty.")
		errors += 1
	
	if len(password) < 8:
		messages.add_message(request, messages.INFO, "Password is too short.")
		errors += 1
	
	if password != confirm_password:
		messages.add_message(request, messages.INFO, "Passwords do not match.")
		errors += 1
	
	hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
	
	if errors == 0:
		messages.add_message(request, messages.INFO, "Registration Successful! Please Log In.")
		User.objects.create(name=name, username=username, password=hashed_password, datehired=datehired)
		user = User.objects.get(username = username)
		request.session['id'] = user.id
		return redirect('/dashboard')
	else:
		return redirect('/')
	
def wish_items(request, item_id):
	if authsession(request):
		return redirect('/')
		
	item = Item.objects.get(id=item_id)
	
	wishlists = Wishlist.objects.filter(items = item)
	
	content = {
		'item': item,
		'wishlists': wishlists
	}
	
	return render(request, 'wishlist/wish_items.html', content)

def create(request):
	authsession(request)
	return render(request, 'wishlist/create.html')
	
def add_item(request):
	if authsession(request):
		return redirect('/')
		
	user = User.objects.get(id = request.session['id'])
	wishlist = Wishlist.objects.filter(users = user).all()
	
	# Creates the item if it doesn't already exist.
	if Item.objects.filter(name=request.POST["name"]).exists():
		item = Item.objects.get(name=request.POST["name"])
	else:
		Item.objects.create(name=request.POST["name"], created_by = user)
		item = Item.objects.get(name=request.POST["name"])
		
	# Adds to the wishlist, if it isn't already there.
	if wishlist.filter(items=item).exists():		
		messages.add_message(request, messages.INFO, 'Item already exists on your wishlist.')		

	else:			
		Wishlist.objects.create(users = user, items = item)		
		messages.add_message(request, messages.INFO, 'Successfully added item to wishlist.')	
	
	return redirect('/dashboard')

def delete(request, item_id):
	if authsession(request):
		return redirect('/')
		
	if request.session['id'] == Item.objects.get(id=item_id).created_by.id:
		item = Item.objects.get(id=item_id)
		item.delete()
		item.save()
		messages.add_message(request, messages.INFO, 'Successfully deletd item.')	
	else:
		wishlist = Wishlist.objects.filter(users = User.objects.get(id=request.session['id']), items = Item.objects.get(id=item_id)).first()
		wishlist.delete()
		messages.add_message(request, messages.INFO, 'Successfully deleted item from wishlist.')	
	
	return redirect('/dashboard')
	
def dashboard(request):
	if authsession(request):
		return redirect('/')
		
	user = User.objects.get(id=request.session['id'])
	wishlist = Wishlist.objects.filter(users = user).all()
	items_ids_on_my_wishlist = wishlist.values_list('items_id', flat=True).distinct()
	all_items_ids = Wishlist.objects.all().values_list('items_id', flat=True).distinct()
	print items_ids_on_my_wishlist
	print all_items_ids
	print Wishlist.objects.exclude(items_id__in = items_ids_on_my_wishlist).all().values_list('items_id', flat=True).distinct()
	print Wishlist.objects.exclude(items_id__in = items_ids_on_my_wishlist).values_list('items_id', flat=True).distinct()
	others_wishlist = Wishlist.objects.exclude(items_id__in = items_ids_on_my_wishlist)
	
	
	# items_created_by_others = Items.objects.exclude(created_by = user).all()
	# items_created_by_others_id = items_created_by_others.values_list('id')
	
	# missing_items_ids = Item.objects.exclude(created_by=user).difference(wishlist.select_related('items').all()).values_list('id')
	# print missing_items_ids
	# get items the current user does not have
	# missing_items = Wishlist.objects.difference(wishlist)
	
	# others_wishlist = Wishlist.objects.filter(items__in=missing_items_ids)
	# exclude_items_user_has = Wishlist.objects.exclude(users = user).all()
	
	content = {
		'user': user,
		'wishlist': wishlist,
		'others_wishlist': others_wishlist
	}
	
	return render(request, 'wishlist/dashboard.html', content)
	
def authsession(request):
	if request.session.get('id', None) is None:
		return false
	else
		return true