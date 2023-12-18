from django import forms
from django.contrib.auth.models import User
from django.forms import fields, SelectDateWidget
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, \
    PasswordResetForm, UsernameField
from django.core import validators
from .models import SubstituicaoAula, Curso
from django.forms import ModelForm


def validete_username(value):
    if len(value) <= 2:
        raise forms.ValidationError(f"Your username cannot be of {len(value)}  word")


class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"placeholder": "Senha", 'autocomplete': 'new-password', 'class': 'form-control input'}),
                                error_messages={"required": "Please enter password"}, )
    password2 = forms.CharField(label="Re-enter", widget=forms.PasswordInput(
        attrs={"placeholder": "Confirme a senha", 'autocomplete': 'new-password', 'class': 'form-control input'}),
                                help_text="Make sure your password contains 'small letter','capital letter','numbers' and 'symbols'",
                                error_messages={"required": "Re-Enter password field cannot be empty"})
    username = forms.CharField(label="username", widget=forms.TextInput(
        attrs={"placeholder": "Nome de usuário", "id": "username", 'class': 'form-control input'}),
                               validators=[validete_username])
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Primeiro nome", "required": True, 'class': 'form-control input'}),
        error_messages={"required": "Primeiro nome não pode ficar vazio."})
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Último nome", "required": True, 'class': 'form-control input'}),
        error_messages={"required": "Último nome não pode ficar vazio."})
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"required": True, "Placeholder": "E-mail", 'autocomplete': 'username', 'class': 'form-control input'}))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"placeholder": "Nome de usuário", 'class': 'form-control input'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Senha", 'autocomplete': 'current-password', 'class': 'form-control input'}))






class FormSubstitua(ModelForm):
    horarios_aula = forms.MultipleChoiceField(
        choices=SubstituicaoAula.HORARIOS_CHOICES.items(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = SubstituicaoAula
        fields = ["data_hora_aula_substituida", "curso_afetado", "horarios_aula", "semestre_afetado"]
        widgets = {
            'data_hora_aula_substituida': SelectDateWidget(),
            'horarios_aula': forms.CheckboxSelectMultiple(),
        }


