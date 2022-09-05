from django import forms
from .models import Message




class MessageForm(forms.ModelForm):
    class Meta:
        model = Message


        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'The Message'}),
        }
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
        }
