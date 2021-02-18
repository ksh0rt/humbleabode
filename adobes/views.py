from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Abode
from django.contrib.auth import authenticate, login
from .forms import AddressForm, AbodeForm

def home(request):
    return render(request, 'abodes/home.html')

def myabodes(request):
    return render(request, 'abodes/myabodes.html')

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

def AddAbode(request):
    address_form = AddressForm
    abode_form = AbodeForm
    return render(request, 'abodes/add_abode.html', {'AddressForm':address_form,'AbodeForm':abode_form})

class DetailAbode(generic.DetailView):
    model = Abode
    template_name = 'abodes/detail_abode.html'

class UpdateAbode(generic.UpdateView):
    model = Abode
    template_name = 'abodes/update_abode.html'
    fields = ['price','street_address','city','state','zip_code','bedrooms','bathrooms','SqFoot','image']
    success_url = reverse_lazy('home')

class DeleteAbode(generic.DeleteView):
    model = Abode
    template_name = 'abodes/delete_abode.html'
    success_url = reverse_lazy('home')
