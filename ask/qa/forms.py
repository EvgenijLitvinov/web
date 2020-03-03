from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=245, help_text='Это поле обязательно')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        aa = Question(**self.cleaned_data)
        aa.author = User.objects.get(id=1)
        aa.save()
        return aa
        

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def save(self, id):
        aa = Question.objects.get(id=id)
        Answer.objects.create(text=self.cleaned_data['text'], author = User.objects.get(id=1), question = aa)
        return aa
    