from django import forms
from .models import Contact

#Burada modelimizde bulunan formumuzun içeriklerini kaydediyoruz.

class ContactForm(forms.ModelForm):
      class Meta:
            model = Contact
            fields = ['name', 'email', 'message','sub']