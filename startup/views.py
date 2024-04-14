from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import SignInForm, SignUpForm, ContactForm, CheckoutForm
from .models import CustomUser, Purchase, QrCode
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, TemplateView
import razorpay
from razorpay import Client  
from django.http import JsonResponse

from django.core.mail import send_mail
from django.conf import settings

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from phonenumber_field.validators import validate_international_phonenumber
import re

from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password



from django.shortcuts import render,get_object_or_404, redirect, reverse
from .models import Category, Product, AnouncementModel
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from decimal import Decimal
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .context_processors import username_data
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                login(request, user=user)
                request.session['username'] = username
                return redirect(reverse('about'))
            else:
                error = 'User Does Not Exist!, Create a New User To Continue.'
                form = SignUpForm
                return render(request, 'signup.html', {'error':error, 'form': form})
                
    form = SignInForm
    return render(request, 'signin.html', {'form':form})






def home(request):

    anouncement = AnouncementModel.objects.all()
    basic_plan = Product.objects.filter(slug='basic-plan')
    standard_plan = Product.objects.filter(slug='standard-plan')
    professional_plan = Product.objects.filter(slug='professional-plan')
    
    return render(request, 'base.html', {'anouncement': anouncement, 'basic_plan':basic_plan, 'standard_plan':standard_plan, 'professional_plan': professional_plan})

class About(TemplateView):
    template_name = 'about.html'


def get_username(request):
    user = request.session.get('username')
    return JsonResponse({'user': user})

def logout_view(request):
    
    logout(request)

    return redirect('home')


class Enquiry(FormView):
    template_name = 'enquiry.html'
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




def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('signin'))
        else:
            error = form.errors
            return render(request, 'signup.html', {'form': form, 'error':error})
            
    form = SignUpForm
    return render(request, 'signup.html', {'form':form})







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
        




# Create your views here.







def checkout(request):
    if request.method == 'POST':
        
        form = CheckoutForm(request.POST)
        if form.is_valid():
            print('form valid')
            form.save()
            print('form saved')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            name = first_name + last_name
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            transaction_id = form.cleaned_data['transaction_id']
            package_price = form.cleaned_data['package_price']
            recipients = ['vikiadhi2016@gmail.com', '8ragu.io@gmail.com']
            message = f"New Customer Attempted to make a payment verify the payment details with your bank transaction details\r\n \r\nTransaction ID: {transaction_id} \r\n \r\n Package Price choosed{package_price}"
          
            if message:
            
                send_mail(recipient_list=recipients, 
                      subject=f'Tokaz New Billing Detils', 
                      message=f'Useraname : {name}\r\n \r\n User Email : {email} \r\n \r\n User Phone Number: {phone_number} \r\n \r\n Message : {message}', 
                      from_email='vikramanm.py@gmail.com')
            
            return redirect(reverse('success'))
    else:
        form = CheckoutForm
    # qr_code = QrCode.objects.first()
    return render(request, 'checkout.html', {'form': form})


def success(request):
    return render(request, 'success.html')



def features(request):
    return render(request, 'our_features.html')



def contact(request):
    return render(request, 'contact.html')