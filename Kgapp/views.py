from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.generics import RetrieveAPIView,ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
import json
from django.core import serializers

class QuestionDetailAPIView(ListCreateAPIView):
	#standard=standard
	#test_id=test_id
	queryset=Question.objects.all()
	serializer_class=QuestionSerializer
	filter_backends=(DjangoFilterBackend,)
	filter_fields=('standard','test_id')
def get_question(request,standard,test_id):
	obj=Question.objects.filter(standard=standard).filter(test_id=test_id)
	
	data = serializers.serialize('json',[ obj, ])
	print(data)
	return HttpResponse(data, content_type='application/json')
	#return render(request,"obj.html",{'obj':obj})
	
	
