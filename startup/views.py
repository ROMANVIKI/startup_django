from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignInForm, SignUpForm, ContactForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, TemplateView


from django.core.mail import send_mail
from django.conf import settings

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from phonenumber_field.validators import validate_international_phonenumber
import re

from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
# Create your views here.

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                login(request, user=user)
                
                return redirect(reverse('cart'))
            else:
                return HttpResponse('<p style="color:red;">User not valid!</p>')
    form = SignInForm
    return render(request, 'signin.html', {'form':form})



class Home(TemplateView):
    template_name = 'main.html'

class About(TemplateView):
    template_name = 'about.html'


class Cart(TemplateView):
    template_name = 'cart.html'






class Contact(FormView):
    template_name = 'contact.html'
    form_class = ContactForm  # Set the form class

    def form_valid(self, form):
        # Save the form data
        form.save()

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        recipients = ['vikiadhi2016@gmail.com', '8ragu.io@gmail.com']
        if message:
            sender = ''
        send_mail(recipient_list=recipients, 
                  subject=f'FROM TRADE TRENCH - Subject : {subject}', 
                  message=f'Useraname : {name}\r\n \r\n User Email : {email} \r\n \r\n User Phone Number: {phone_number} \r\n \r\n Message : {message}', 
                  from_email='vikramanm.py@gmail.com')

        # Redirect to success URL
        return super().form_valid(form)

    def get_success_url(self):
        # Define the success URL where the user should be redirected after successful form submission
        return reverse_lazy('home')




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('signin'))
        else:
            return HttpResponse(form.errors)
    form = SignUpForm
    return render(request, 'signup.html', {'form':form})



def dashborad(request):
    return render(request, 'nav.html')



# For signup validation through htmx

def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if get_user_model().objects.filter(username=username).exists():
            return HttpResponse('<p style="color: red;">Username already exists.</p>')
        else:
            return HttpResponse('<p style="color:green;">Username available.</p>')
        


def check_mobile_number(request):
    mobile_num = request.POST.get('mobile_number')
    if get_user_model().objects.filter(mobile_number=mobile_num).exists():
        return HttpResponse('<p style="color: red;">Mobile number already exists.</p>')
    else:
        return HttpResponse('<p></p>')


def check_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            # Validate email format
            validate_email(email)
        except ValidationError:
            # Return error response if email is not valid
            return HttpResponse('<p style="color: red;">Invalid email format.</p>')

        if get_user_model().objects.filter(email=email).exists():
            # Return error response if email already exists in the database
            return HttpResponse('<p style="color: red;">Email already exists.</p>')
        else:
            # Return success response if email is valid and does not exist in the database
            return HttpResponse('<p style="color: green;">Email available.</p>')
        


def check_password(request):
    if request.method == 'POST':
        password = request.POST.get('password1')

        try:
            validate_password(password=password)
            return HttpResponse('<p style="color: green;">Good to go!</p>')
        except ValidationError as e:
            return HttpResponse(f'<p style="color: red;">{e}</p>')

# ------------------------------ 
        


# for login validation through htmx 

# def check_username_password(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             return HttpResponse('<p></p>')
#         else:
#             return HttpResponse('<p style="color: red;">Invalid username or password.</p>')

