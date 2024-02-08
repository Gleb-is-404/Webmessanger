from django.db import models
# Create your models here.
class chat(models.Model):
	create_time=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=28)
	text=models.TextField()
	like=models.IntegerField()
	class Meta:
		db_table = 'chat'
class user(models.Model):
	create_time=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=28)
	password = models.CharField(max_length=28)
	class Meta:
		db_table = 'user'
