from django import forms

from morphology.core.domain import CASES, NUMBERS

OPERATIONS = [("normal", "Normal form"), ("grammar", "Grammar"), ("inflect", "Inflect")]


class OperationForm(forms.Form):
    operation = forms.ChoiceField(choices=OPERATIONS, label="")


class TextForm(forms.Form):
    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"rows": 4}))


class InflectForm(TextForm):
    case = forms.ChoiceField(choices=list(CASES.items()), label="Падеж")
    number = forms.ChoiceField(choices=list(NUMBERS.items()), label="Число")
