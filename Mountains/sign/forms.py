#
# #ЭТО ВТОРОЙ ВАРИАНТ и НА МОЙ ВЗГЛЯД ПРАВИЛЬНЫЙ !!!!
#                         # Напишем форму, с помощью которой мы будем создавать нового пользователя.
#
# from django.contrib.auth.forms import UserCreationForm                   # Для изменения стандартной модели пользователя
# from sign.models import UserProfile
# from django import forms
#
# ########################################################################################################################
#
# class BaseRegisterForm(UserCreationForm):
#     # Добавляем поля в форму
#     email = forms.EmailField(label = "Email")
#     name = forms.CharField(label = "Имя")
#     surname = forms.CharField(label = "Фамилия")
#     otchestvo = forms.CharField(label = "Отчество")
#     phone = forms.CharField(label = "Номер телефона")
#
#     class Meta:
#         model = UserProfile
#         fields = ("user",
#                   "name",
#                   "surname",
#                   "otchestvo",
#                   "email",              # Поле по умолчанию
#                   "phone",
#                   "password1",          # Поле по умолчанию
#                   "password2", )        # Поле по умолчанию
#
# ########################################################################################################################