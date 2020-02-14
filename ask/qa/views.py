from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def man(request):
	questions = Question.objects.new()
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, 10)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'qa/main.html', {
		'questions': page.object_list,
		'paginator': paginator, 'page': page
	})

def quest(request, id):
	qu = get_object_or_404(Question, id=id)
	try:
		an = Answer.objects.filter(question=qu)
	except Answer.DoesNotExist:
		an = None
	return render(request, 'qa/question.html', {'qu': qu, 'an': an})
