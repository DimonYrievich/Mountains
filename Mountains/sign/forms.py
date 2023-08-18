
                        # Напишем форму, с помощью которой будет создаваться новый пользователь.

from django.contrib.auth.forms import UserCreationForm                   # Для изменения стандартной модели пользователя
from django.contrib.auth.models import User                                # Импортируем стандартную модель пользователя
from django import forms
from Point.models import Users

########################################################################################################################

class BaseRegisterForm(UserCreationForm):
    # Добавляем поля в форму, если их нет в стандартной модели
    email = forms.EmailField(label = "Email")
    name = forms.CharField(label = "Ваше имя")
    surname = forms.CharField(label = "Фамилия")
    otchestvo = forms.CharField(label = "Отчество")
    phone = forms.CharField(label = "Номер телефона")

    class Meta:
        model = User
        fields = [
            "username",                                       # Поле по умолчанию
            "name",
            "surname",
            "otchestvo",
            "email",
            "phone",
            "password1",                                      # Поле по умолчанию
            "password2",                                      # Поле по умолчанию
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ""                # Убираем текст подсказки
        self.fields["password1"].help_text = ""               # Убираем текст подсказки
        self.fields["password2"].help_text = ""               # Убираем текст подсказки
        self.fields["username"].label = "Как Вас называть"    # Изменяем название поля
        self.fields["password1"].label = "Пароль"             # Изменяем название поля
        self.fields["password2"].label = "Повторите пароль"   # Изменяем название поля

########################################################################################################################
                # Форма для Users, чтобы обрабатывать дополнительные данные, отличные от стандартных

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['phone', 'surname', 'name', 'otchestvo']

########################################################################################################################