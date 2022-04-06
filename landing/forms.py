from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=40)
    message = forms.CharField(max_length=300, widget=forms.Textarea)
