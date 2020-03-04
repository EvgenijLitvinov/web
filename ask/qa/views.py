from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login


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

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
		username=form.cleaned_data['username']
		password=form.cleaned_data['password1']
		user = authenticate(username=username, password=password)
		print(user)
		return redirect('main')
	else:
		form = SignUpForm()
		return render(request, 'qa/signup.html', {'form': form})

def quest(request, id):
	qu = get_object_or_404(Question, id=id)
	try:
		an = Answer.objects.filter(question=qu)
	except Answer.DoesNotExist:
		an = None
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			ans = form.save(id)
			return HttpResponseRedirect(ans.get_url())
	else:
		form = AnswerForm(initial={'text': '', 'question': id})
	return render(request, 'qa/question.html', {'qu': qu, 'an': an, 'form': form})

def askk(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			ask = form.save()
			return HttpResponseRedirect(ask.get_url())
	else:
		form = AskForm()
	return render(request, 'qa/ask_add.html', {'form': form})

def popul(request):
	questions = Question.objects.popular()
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, 10)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page)
	return render(request, 'qa/main.html', {
		'questions': page.object_list,
		'paginator': paginator, 'page': page
	})
