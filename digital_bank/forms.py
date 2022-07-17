from django import forms
from django.forms import ModelForm
from .models import Contas, Historico


class NewAccForm(ModelForm):
    class Meta:
        model = Contas
        fields = ('nome', 'cpf', 'rg', 'celular', 'endereco', 'cep', 'email', 'saldo')

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Insira o nome'}),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Insira o CPF (ex:12345678900)'}),
            'rg': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Insira o RG (ex:1234567890000)'}),
            'celular': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Insira o celular (ex:81999999999)'}),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Insira o endereco'}),
            'cep': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Insira o CEP (ex:99999999)'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Insira o email (ex:exemplo@exemplo.com)'}),
            'saldo': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Insira o saldo inicial'})
        }
