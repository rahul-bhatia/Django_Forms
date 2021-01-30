from django import forms


class ACFroms(forms.Form):
	radius=forms.FloatField(label="Enter radius",min_value=0)

