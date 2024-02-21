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
                return HttpResponse('User not valid!')
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
        recipients = ['vikiadhi2016@gmail.com']
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





def check_username(request):
    username = request.POST.get(username)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('Username already exists.')
    else:
        return HttpResponse('Username Available.')