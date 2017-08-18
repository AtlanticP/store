from django import forms

class ItemForms(forms.Form):

	item_logo = forms.FileField()
	name = forms.CharField(max_length = 200)
	description = forms.CharField(max_length = 500)
	price_of_income = forms.IntegerField()
	price_of_sold = forms.IntegerField()
	interests = forms.IntegerField()