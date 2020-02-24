from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User

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
    question = forms.CharField()

    def save(self):
        pass
    