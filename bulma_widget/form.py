from django import forms
from . import widgets


class TestForm(forms.Form):
    text = forms.CharField(max_length=5, widget=widgets.BulmaTextInput)
    number = forms.FloatField(widget=widgets.BulmaNumberInput)
    password = forms.CharField(max_length=5, widget=widgets.BulmaPasswordInput)
    email = forms.EmailField(widget=widgets.BulmaEmailInput)
    select = forms.ChoiceField(widget=widgets.BulmaSelect)
    multi_select = forms.MultipleChoiceField(widget=widgets.BulmaMultiSelect)
    files = forms.FileField(widget=widgets.BulmaFileInput)
    date = forms.DateField(widget=widgets.BulmaDateInput)
    text_area = forms.CharField(max_length=5, widget=widgets.BulmaTextarea)
