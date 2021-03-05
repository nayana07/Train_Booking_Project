from django import forms
from django.core.exceptions import ValidationError
from .models import booking


# Create your models here.

class Booking_form(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'
        