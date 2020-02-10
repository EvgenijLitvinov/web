from django.shortcuts import render

# Create your views here.
from qa.models import Question
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def quest(request, id):
	try:
		ss = Question.objects.all()[:1]
	except Question.DoesNotExist:
		ss = 'nea'
	ans = 'ID = ' + str(id) + "<br>"
	ans += str(ss)
	return HttpResponse(ans)
