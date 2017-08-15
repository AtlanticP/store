from django.db import models

class ItemsModels(models.Model):

	item_logo = models.FileField()
	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 500)
	price_of_income = models.IntegerField()
	price_of_sold = models.IntegerField()

