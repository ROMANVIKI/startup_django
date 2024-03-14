from .models import CustomUser, ContactModel, CheckoutModel
from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


# name email phone number subject message



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone_number', 'subject', 'message']
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message'


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckoutModel
        fields = [
            'first_name', 'last_name',
            'company_name', 'country', 
            'street_address', 'city', 
            'state', 'zipcode', 'email'
            ]

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Company Name'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        self.fields['street_address'].widget.attrs['placeholder'] = 'Street Address'
        self.fields['city'].widget.attrs['placeholder'] = 'City'
        self.fields['state'].widget.attrs['placeholder'] = 'State'
        self.fields['zipcode'].widget.attrs['placeholder'] = 'Zipcode'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'





class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2', 'mobile_number', 'referral_code']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['mobile_number'].widget.attrs['placeholder'] = 'Mobile Number'
        self.fields['referral_code'].widget.attrs['placeholder'] = 'Referral Code (Optional)'
        self.fields['mobile_number'].initial = "+91"


