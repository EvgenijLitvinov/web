from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(max_length=245)
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        return User.objects.create_user(**self.cleaned_data)



class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        aa = Question(**self.cleaned_data)
        aa.author = User.objects.get(username=self._user)
        aa.save()
        return aa
        

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def save(self, id):
        aa = Question.objects.get(id=id)
        Answer.objects.create(text=self.cleaned_data['text'], author = User.objects.get(username=self._user), question = aa)
        return aa
    