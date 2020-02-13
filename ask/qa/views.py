from django.shortcuts import render, get_object_or_404

# Create your views here.
from qa.models import Question, Answer
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def man(request):
	page = request.GET.get('page')
	return HttpResponse(page)

def quest(request, id):
	qu = get_object_or_404(Question, id=id)
	try:
		an = Answer.objects.filter(question=qu)
	except Answer.DoesNotExist:
		an = None
	return render(request, 'qa/question_pattern.html', {'qu': qu, 'an': an})
