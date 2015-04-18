from django.db import models
from django.contrib.auth.models import User
from product.models import *
# Create your models here.

class UserProfile(models.Model):
	user= models.OneToOneField(User)
	profile_pic=models.ImageField(upload_to = 'profile_pics/',blank=True)
	phone_number=models.CharField(max_length = 10,blank=True)
	city = models.ForeignKey(City)
	address=models.CharField(max_length=50)
	cart_info=models.ManyToManyField(Entry)
	
	class Meta:
		db_table = 'profile'
	def __str__(self):
		return self.user.username
class Status(models.Model):
	type_s=models.CharField(max_length=20)

class Order(models.Model):
	user=models.ForeignKey(UserProfile)
	product=models.ForeignKey(Entry)
	placed_time=models.DateTimeField(auto_now_add=True)
	delivery_status=models.ForeignKey(Status)
