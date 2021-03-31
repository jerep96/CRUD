from django.shortcuts import render
from .form import LoginForm


# Create your views here.
def login(request):
    form = LoginForm()
    contexto = {
        'form': form,
        'class': 'form-control item'
    }
    return render(request, 'general_login.html', contexto)
