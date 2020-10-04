from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.admin.views.decorators import staff_member_required


from django.contrib import messages

from .forms import CreateUserForm
# Create your views here.

@staff_member_required
def results(request, question_id):
    response = "You're looking at the results of feedback %s."
    return HttpResponse(response % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'palaute/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'palaute/detail.html', {'question': question})


def vote(request, question_id):
    return HttpResponse("You're giving feedback on topic %s." % question_id)

def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Tili on luotu käyttäjälle' + user)
            #return redirect('login')
            #return redirect('/palaute/login/')

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
            #return redirect('index')
            return redirect ('/palaute/index/')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {'form':form}
    return render(request, 'palaute/login.html', context)

