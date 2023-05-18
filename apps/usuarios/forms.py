from django import forms
from django.contrib.auth.models import User, Group

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    

    def clean_nome_login(self):
        nome = self.cleaned_data.get('nome_login')

        if nome:
            nome = nome.strip()
            validacao = User.objects.filter(username=nome).exists()

            if not validacao:
                raise forms.ValidationError('Nome de usuário não cadastrado!')
            
            return nome


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João"
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )


    def clean(self):
        cleaned_data = super().clean()

        senha_1 = cleaned_data.get('senha_1')
        senha_2 = cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas não são iguais!')
            
            return cleaned_data


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            email = email.strip()

            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email já cadastrado!')

            return email
    

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()

            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            
            elif User.objects.filter(username=nome).exists():
                raise forms.ValidationError('Nome de usuário já cadastrado!')
                
            return nome

    
    def save(self, commit=True):
        nome = self.cleaned_data.get('nome_cadastro')
        email = self.cleaned_data.get('email')
        senha = self.cleaned_data.get('senha_1')
        usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )
        
        if commit:
            usuario.save()

            grupo = Group.objects.filter(pk=1).first()

            if grupo:
                usuario.groups.add(grupo)
                usuario.save()
            
        return usuario
