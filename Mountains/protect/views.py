
                                        # ПРОВЕРКА/АУТЕНТИФИКАЦИЯ

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy                                 # Импортируем reverse_lazy для создания URL-адресов

########################################################################################################################

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'
    success_url = reverse_lazy('myprofile')    # Используем reverse_lazy для определения URL-адреса после футентификации