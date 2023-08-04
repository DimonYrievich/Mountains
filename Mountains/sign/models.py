
                        # Напишем форму, с помощью которой мы будем создавать нового пользователя.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BaseRegisterForm(UserCreationForm):
    # Добавляем поля в форму
    email = forms.EmailField(label = "Email")
    name = forms.CharField(label = "Имя")
    surname = forms.CharField(label = "Фамилия")
    otchestvo = forms.CharField(label = "Отчество")
    phone = forms.CharField(label = "Номер телефона")

    class Meta:
        model = User
        fields = ("username",           # Поле по умолчанию
                  "name",
                  "surname",
                  "otchestvo",
                  "email",              # Поле по умолчанию
                  "phone",
                  "password1",          # Поле по умолчанию
                  "password2", )        # Поле по умолчанию