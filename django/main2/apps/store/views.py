# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, "store/index.html")
	
def buy(request):
	print request.POST
	product_id = int(request.POST['product_id'])
	items_bought = int(request.POST['quantity'] or 0)
	cost = 0.00
	total_items_bought = int(request.session.get('total_items_bought') or 0)
	total_cost = float(request.session.get('total_cost') or 0)
	
	# Will use a if statement, but usually, this would  be a database query.
	if product_id == 1:
		cost = 19.99
	elif product_id == 2:
		cost = 29.99
	elif product_id == 3:
		cost = 4.99
	elif product_id == 4:
		cost = 49.99
		
	if product_id > 0:
		total_items_bought += items_bought	
		total_cost = total_cost + cost * items_bought
		
	request.session['total_items_bought'] = total_items_bought
	request.session['total_cost'] = total_cost
	charge = cost * items_bought
	
	request.session['charge'] = charge
	
	return HttpResponseRedirect("/amadon/checkout")
	
def checkout(request):
	content = {
		'charge': '%.2f' % float(request.session['charge']),
		'total_items_bought': request.session['total_items_bought'],
		'total_cost': request.session['total_cost']
	}
	
	del request.session['charge']
	return render(request, 'store/checkout.html', content)