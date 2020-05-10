from django import forms
from operations.json.json import JsonFileOperator
from operations.config.config import Config


class TextForm(forms.Form):
    """Класс описывает ограничения и поля формы проверки задачи"""
    word = forms.CharField(label = 'Your name', widget = forms.Textarea())


class SelectorForm(forms.Form):
    CHOICES = [('/normal', 'NormalForm'), ('/grammar', 'Grammar'), ('/inflect', 'Inflect')]
    services = forms.ChoiceField(widget = forms.Select(choices = CHOICES), choices = CHOICES, label = '')


class POSSelector(forms.Form):
    CHOICES = JsonFileOperator.read(Config().get('morph', 'cases'))
    CHOICES = [(key, value) for key, value in CHOICES.items()]
    services = forms.ChoiceField(widget = forms.Select(choices = CHOICES), choices = CHOICES, label = '')


class NumSelector(forms.Form):
    CHOICES = JsonFileOperator.read(Config().get('morph', 'numbers'))
    CHOICES = [(key, value) for key, value in CHOICES.items()]
    services = forms.ChoiceField(widget = forms.Select(choices = CHOICES), choices = CHOICES, label = '')
