from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):
	name=models.CharField(max_length=30, unique=True)
	class Meta:
		'''table_name= 'Country'''
		verbose_name_plural= 'countries'
	def __str__(self):
		return self.name
class State(models.Model):
	country=models.ForeignKey(Country)
	name=models.CharField(max_length=50)
	class Meta:
		'''table_name='state'''
	def __str__(self):
		return self.name + ',' + self.country.name

class City(models.Model):
	state=models.ForeignKey(State)
	name=models.CharField(max_length=50)
	class Meta:
		'''table_name='city'''
		verbose_name_plural= 'cities'
	def __str__(self):
		return self.name + ',' + self.state.name + ',' +self.state.country.name

class Type(models.Model):
	name=models.CharField(max_length=30)

class Product(models.Model):
	name=models.CharField(max_length=30, blank=True)
	code=models.CharField(unique=True,max_length=20)
	type_of=models.ForeignKey(Type)
	pic=models.ImageField(upload_to='product_pics/',blank=True)	

class Gold(models.Model):
	karat=models.IntegerField()
	price_per_gram=models.IntegerField()

class Diamond_class(models.Model):
	name=models.CharField(max_length=20)

class Entry(models.Model):
	code=models.ForeignKey(Product)
	weight=models.IntegerField()
	karat=models.ForeignKey(Gold)
	diamond=models.IntegerField(null=True)
	diamond_type=models.ForeignKey(Diamond_class)
	stone=models.IntegerField(null=True)
	stone_string=models.CharField(blank=True,max_length=50)
	uncut_diamond=models.CharField(blank=True,max_length=50)
	making=models.IntegerField()
	added_on=models.DateTimeField(auto_now_add=True)
	in_stock=models.IntegerField(default=1)

	
	
