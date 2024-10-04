from django import forms
from .models import UserMessage

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            
        }
    


