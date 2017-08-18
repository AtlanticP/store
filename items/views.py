from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import ItemsModels

from django.http import HttpResponse
import os

# class ItemView_template(TemplateView):

# 	template_name = 'items/index.html'

# class ItemListView(ListView):

# 	model = ItemsModels 
# 	template_name = 'items/index.html'

# 	def interest(self):
# 		return (self.price_of_sold-self.price_of_income) 

def index(request):
	all_items = ItemsModels.objects.all()
	
	for item in all_items:
		item.interests = item.price_of_sold - item.price_of_income
		item.save()

	return render(request, 'items/index.html', {'all_items': all_items})


def get_root(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	return HttpResponse(STATIC_ROOT+'\items\css\style.css')










