from django import forms
from .models import ContactModel

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'