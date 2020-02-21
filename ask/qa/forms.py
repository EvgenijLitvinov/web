from django import forms

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField()

class AnswerForm(forms.Form):
    text = forms.CharField()
