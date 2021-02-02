from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Abode

def home(request):
    return render(request, 'abodes/home.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

class AddAbode(generic.CreateView):
    model = Abode
    fields = ['price','street_address','city','state','zip_code','bedrooms','bathrooms','SqFoot','image']
    template_name = 'abodes/add_abode.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(AddAbode, self).form_valid(form)
        return redirect('home')
