from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('email', 'subject', 'body')
        widgets = {
            'email': forms.TextInput(attrs={'id': 'email', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'id': 'subject', 'placeholder': 'Subject'}),
            'body': forms.Textarea(attrs={'id': 'body', 'placeholder': 'Message'}),
        }