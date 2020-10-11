from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, PalauteForm

# Create your views here.

def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Tili on luotu onnistuneesti käyttäjälle: ' + user)
            return redirect('palaute:login')

    context = { 'form':form}
    return render(request, 'palaute/register.html', context)


def login_page(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('palaute:feedback')
        else:
            messages.info(request, 'Tunnus TAI salasana on väärin')

    context = {'form':form}
    return render(request, 'palaute/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('palaute:login')

@login_required(login_url='palaute:login')
def feedback(request):
    form = PalauteForm(initial={'FK_toimipiste_id':'1'})

    if request.method == 'POST':
        form = PalauteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('palaute:feedback')
            
    messages.info(request, 'Kiitos palautteestasi')
    context = {'form':form}
    return render(request, 'palaute/index.html', context)

#def results(request, question_id):
#    response = "You're looking at the results of feedback %s."
#    return HttpResponse(response % question_id)
