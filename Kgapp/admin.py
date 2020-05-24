from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	list_display=['standard','test_id','question','option_1','option_2','option_3','option_4','answer',]
	
	class meta:
		model=Question
admin.site.register(Question,QuestionAdmin)
