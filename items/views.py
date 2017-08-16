from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ItemsModels

from django.http import HttpResponse
import os
class ItemView_template(TemplateView):

	template_name = 'items/index.html'

def get_root(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	return HttpResponse(STATIC_ROOT+'\items\css\style.css') 








