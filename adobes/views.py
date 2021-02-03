from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Abode
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'abodes/home.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

class AddAbode(generic.CreateView):
    model = Abode
    fields = ['price','street_address','city','state','zip_code','bedrooms','bathrooms','SqFoot','image']
    template_name = 'abodes/add_abode.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(AddAbode, self).form_valid(form)
        return redirect('home')
