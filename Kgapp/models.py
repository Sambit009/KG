from django.db import models

# Create your models here.
class Question(models.Model):
	standard=models.CharField(max_length=50)
	test_id=models.CharField(max_length=50)
	question_id=models.AutoField(primary_key=True)
	question=models.TextField() 
	
	option_1=models.TextField(blank=True) 
	option_2=models.TextField(blank=True) 
	option_3=models.TextField(blank=True) 
	option_4=models.TextField(blank=True) 
	answer=models.TextField(blank=True)
	
	def __str__(self):
		return self.question
	
	
