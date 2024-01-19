from django import forms
from .models import Customers
from django.core.exceptions import ValidationError

class SigninForm(forms.Form):
    cemail = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Email', 'autocomplete': 'off'}))
    cpassword = forms.CharField(max_length=100, min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'off'}), required=True)

class SignupForm(forms.Form): 
    cname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    cemail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    cpassword = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    cre_password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder': 'Repeat your password'}))

    def clean_cemail(self):
        cemail = self.cleaned_data.get('cemail').lower()
        new = Customers.objects.filter(cemail=cemail)
        if new.exists():
            raise ValidationError("Email Already Exists")
        return cemail
    
    def clean_cre_password(self):
        cre_password = self.cleaned_data.get('cre_password')
        password = self.cleaned_data.get('cpassword')

        if cre_password != password:
            raise ValidationError("Passwords do not match")
        return cre_password
    
    def save(self):
        customer = Customers.objects.create(cemail=self.cleaned_data['cemail'], cpassword=self.cleaned_data['cpassword'], cname=self.cleaned_data['cname'])
        return customer
    
class AddtoCart(forms.Form):
    prodid = forms.IntegerField(widget=forms.HiddenInput())