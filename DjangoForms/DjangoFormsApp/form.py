from django import forms

class EoForm(forms.Form):
	num=forms.IntegerField(label="Enter a number")
