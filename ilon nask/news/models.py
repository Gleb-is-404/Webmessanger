from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class chat(models.Model):
	create_time=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=28)
	text=models.TextField()
	like=models.IntegerField()
	emo = ArrayField(models.CharField(max_length=29), default=list)
	files = models.FileField(upload_to='uploads/', default='f.txt')
	class Meta:
		db_table = 'chat'
class user(models.Model):
	create_time=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=28)
	password = models.CharField(max_length=28)
	class Meta:
		db_table = 'user'
class image(models.Model):
	image = models.BinaryField()
	class Meta:
		db_table = 'image'
