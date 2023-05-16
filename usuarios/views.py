from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import auth
from usuarios.forms import LoginForms, CadastroForms


def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        
        if usuario is not None:
            auth.login(request, usuario)

            return redirect('index')
        
        else:
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})
