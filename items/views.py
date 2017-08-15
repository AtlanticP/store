from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ItemsModels

class ItemView_template(TemplateView):

	template_name = 'store/index.html'





