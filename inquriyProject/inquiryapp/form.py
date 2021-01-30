from django import forms

class InquiryForm(forms.Form):
	name=forms.CharField(label="Enter Name")
	email=forms.EmailField(label="Enter email")
	phone=forms.IntegerField(label="Enter Phone number")
