from django import forms

class FbForm(forms.Form):
	name=forms.CharField(label="Enter name")
	feedback=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':23,'style':{'resize':None}}))
