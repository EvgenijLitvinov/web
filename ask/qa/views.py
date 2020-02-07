from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def quest(request, id):
	ans = 'ID=' + str(id) + '\n'
	ans += str(request.GET)
	return HttpResponse(ans)
