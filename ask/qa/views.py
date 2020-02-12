from django.shortcuts import render, get_object_or_404

# Create your views here.
from qa.models import Question, Answer
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def quest(request, id):
	qu = get_object_or_404(Question, id=id)
	an = Answer.objects.filter(question=qu)
	return render(request, 'qa/index.html', {'qu': qu, 'an': an})
