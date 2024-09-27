from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(label='ชื่อ', required=False)
       
class SearchRead(forms.Form):
    name = forms.CharField(label='ชื่อ', required=False)