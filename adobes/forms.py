from .models import Abode, Address
from django import forms

class AddressForm(forms.ModelForm):
    model = Address
    fields = ['street_address', 'city', 'state', 'zip_code']

class AbodeForm(forms.ModelForm):
    model = Abode
    fields = ['price','bedrooms','bathrooms','SqFoot','image','is_sold']
