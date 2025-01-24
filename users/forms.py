# forms.py
from django import forms
from users.models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
        'fname','mname','lname','email',
        'course','qualification','batch',
        'passingyear','mobnumber','dist'
        ]
