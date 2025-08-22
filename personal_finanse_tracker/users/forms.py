from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


# -----------------------------
# Форма регистрации
# -----------------------------
class CustomUserCreationForm(UserCreationForm):
    avatar = forms.ImageField(required=False)
    default_currency = forms.ChoiceField(
        choices=[
            ("RUB", "₽ Рубли"),
            ("USD", "$ Доллары"),
            ("EUR", "€ Евро"),
        ],
        initial="RUB"
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "avatar", "default_currency", "password1", "password2")


# -----------------------------
# Форма логина
# -----------------------------
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "password"]