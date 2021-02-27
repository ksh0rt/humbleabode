from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
import pdb
from django.contrib.auth.forms import UserCreationForm
from .models import Abode, Address, Interest
from django.contrib.auth import authenticate, login
from .forms import AddressForm, AbodeForm


def home(request):
    return render(request, 'abodes/home.html')

def MyAbodes(request):
    current_user = request.user
    abodes = Abode.objects.get(user__exact=current_user)
    return render(request, 'abodes/myabodes.html',{'abodes':abodes})

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

def all(items):
    import operator
    return reduce(operator.and_, [bool(item) for item in items])

def get_address(number):
    return Address.objects.get(address_id=number)

def AddAbode(request):
    address_form = AddressForm()
    abode_form = AbodeForm()
    if request.method == 'POST':
        filled_address_form = AddressForm(request.POST, instance=Address())
        filled_abode_form = AbodeForm(request.POST, request.FILES, instance=Abode())
        if filled_address_form.is_valid() and filled_abode_form.is_valid():
            new_address = filled_address_form.save()
            new_abode = Abode()
            new_abode.price = filled_abode_form.cleaned_data['price']
            new_abode.bedrooms = filled_abode_form.cleaned_data['bedrooms']
            new_abode.bathrooms = filled_abode_form.cleaned_data['bathrooms']
            new_abode.SqFoot = filled_abode_form.cleaned_data['SqFoot']
            new_abode.image = filled_abode_form.cleaned_data['image']
            new_abode.is_sold = filled_abode_form.cleaned_data['is_sold']
            new_abode.image = filled_abode_form.cleaned_data['image']
            current_user = request.user
            new_abode.user = current_user
            new_abode.address = new_address
            new_abode.save()
            return redirect('home')
    return render(request, 'abodes/add_abode.html', {'AddressForm':address_form,'AbodeForm':abode_form})

def DetailAbode(request, pk):
    abode = Abode.objects.get(pk=pk)
    return render(request, 'abodes/detail_abode.html', {'abode':abode})

def Interested(request, pk):
    user = request.user
    abode = Abode.objects.get(pk=pk)
    interests = Interest.objects.filter(user=user)
    for i in interests:
        if i.user == request.user and i.abode == abode:
            return render(request, 'abodes/detail_abode.html', {'abode':abode, 'error':'You have already saved this abode'})
    new_interest = Interest()
    new_interest.user = request.user
    new_interest.abode = abode
    new_interest.save()
    return redirect('home')

def UpdateAbode(request, pk):
    current_abode = Abode.objects.get(pk=pk)
    current_address = current_abode.address
    address_form = AddressForm(instance=current_address)
    abode_form = AbodeForm(instance=current_abode)
    if request.method == 'POST':
        filled_address_form = AddressForm(request.POST, instance=Address())
        filled_abode_form = AbodeForm(request.POST, request.FILES, instance=Abode())
        if filled_address_form.is_valid() and filled_abode_form.is_valid():
            current_address.street_address = filled_address_form.cleaned_data['street_address']
            current_address.city = filled_address_form.cleaned_data['city']
            current_address.state = filled_address_form.cleaned_data['state']
            current_address.zip_code = filled_address_form.cleaned_data['zip_code']
            current_address.save()
            current_abode.price = filled_abode_form.cleaned_data['price']
            current_abode.bedrooms = filled_abode_form.cleaned_data['bedrooms']
            current_abode.bathrooms = filled_abode_form.cleaned_data['bathrooms']
            current_abode.SqFoot = filled_abode_form.cleaned_data['SqFoot']
            current_abode.image = filled_abode_form.cleaned_data['image']
            current_abode.is_sold = filled_abode_form.cleaned_data['is_sold']
            current_abode.image = filled_abode_form.cleaned_data['image']
            current_abode.address = current_address
            current_abode.save()
            return redirect('home')
    else:
        return render(request, 'abodes/update_abode.html', {'abode':current_abode, 'AddressForm':address_form,'AbodeForm':abode_form})

class DeleteAbode(generic.DeleteView):
    model = Abode
    template_name = 'abodes/delete_abode.html'
    success_url = reverse_lazy('home')
