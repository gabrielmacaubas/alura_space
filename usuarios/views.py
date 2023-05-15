from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from usuarios.forms import LoginForms, CadastroForms


def login(request):
    form = LoginForms()

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})
