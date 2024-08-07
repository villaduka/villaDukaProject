from django import forms
from .models import Message



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'