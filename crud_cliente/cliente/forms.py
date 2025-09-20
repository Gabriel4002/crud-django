from .models import Cliente
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)  # Captura o usuário passado pela view
        super().__init__(*args, **kwargs)

        # Adiciona classe 'form-control' a todos os campos
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone:
            if not re.match(r'^[0-9+\-\s\(\)]+$', telefone):
                raise forms.ValidationError('Telefone contém caracteres inválidos.')
            if len(telefone) < 8:
                raise forms.ValidationError('Telefone muito curto.')
        return telefone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.usuario:
            qs = Cliente.objects.filter(usuario=self.usuario, email=email)

            # Se estiver editando, ignora o próprio registro
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise forms.ValidationError('Você já cadastrou um cliente com esse e-mail.')
        return email


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adiciona classe 'form-control' a todos os campos
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
