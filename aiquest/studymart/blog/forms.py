from django import forms
class Teachersregistration(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    email=forms.EmailField()
     