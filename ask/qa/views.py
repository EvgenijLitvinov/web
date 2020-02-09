from django.shortcuts import render

# Create your views here.
from qa.models import Question
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def quest(request, id):
	ans = 'ID = ' + str(id) + "<br>"
	ans += str(dict(request.GET)) + "<br>"
	return HttpResponse(ans)
