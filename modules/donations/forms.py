from django import forms
from .models import Donation


class DonationForm(forms.Form):
    amount = forms.DecimalField(decimal_places=2, max_digits=10)
