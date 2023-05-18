from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import auth
from django.contrib import messages
from apps.usuarios.forms import LoginForms, CadastroForms


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
                messages.success(request, f'{nome} logado com sucesso!')

                return redirect('index')

            form.add_error('__all__', 'Usuário ou senha inválidos!')

    return render(request, 'usuarios/login.html', {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')

    return redirect('login')
