
                                        # РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm
from django.urls import reverse_lazy                                 # Импортируем reverse_lazy для создания URL-адресов
from .forms import UsersForm

########################################################################################################################

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = reverse_lazy('myprofile')       # Используем reverse_lazy для определения URL-адреса после регистрации

    # Cоздаём экземпляр формы UsersForm, проверяем ее на валидность и сохраняем дополнительные данные в таблице Users
    def form_valid(self, form):
        response = super().form_valid(form)

        profile_form = UsersForm(self.request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = self.object
            profile.save()

        return response

########################################################################################################################