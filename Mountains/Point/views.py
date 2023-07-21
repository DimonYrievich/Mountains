from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
# from .filters import PointFilter
# from .forms import PointForm


class PointsList(ListView):              # ПРЕДСТАВЛЕНИЕ. Для отображения всех точек на всех перевалах.
    model = Point                        # Указываем модель, объекты которой мы будем выводить
    template_name = 'points_list.html'   # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'points'       # Имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 4                      # ПАГИНАЦИЯ. Количество записей на web-странице + нужно внести изменения в шаблоне HTML

#     # Фильтрация
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = PointFilter(self.request.GET, queryset)
#         return self.filterset.qs.order_by('-time_in')
#     # Фильтрация
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filterset'] = self.filterset
#         return context


class MypointsList(LoginRequiredMixin, ListView):          # ПРЕДСТАВЛЕНИЕ. Для отображения СПИСКА всех своих публикаций
    model = Point
    template_name = 'mypoints_list.html'
    context_object_name = 'mypoints'
    paginate_by = 4
#
#     # Фильтрация
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = MypointsFilter(self.request.GET, queryset=queryset)
#         #return Point.objects.filter(user__name_user=self.request.user).order_by('-time_in') - так было до добавления фильтрации
#         return self.filterset.qs.filter(user__name_user=self.request.user).order_by('-time_in')
#     # Фильтрация
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filterset'] = self.filterset
#         return context


# class PointDetail(DetailView):          #ПРЕДСТАВЛЕНИЕ Для отображения одного экземпляра таблицы из БД.
#     model = Point
#     template_name = 'point_detail.html'
#     context_object_name = 'point'


# class PointCreate(CreateView, PermissionRequiredMixin):   #ПРЕДСТАВЛЕНИЕ для создания публикации
#     form_class = PointForm
#     model = Point
#     template_name = 'point_create.html'


# class PointUpdate(UpdateView, LoginRequiredMixin):     #ПРЕДСТАВЛЕНИЕ для изменения публикации.
#     form_class = PointForm                             #Будем использовать ту же форму, что и для создания публикации
#     model = Point
#     template_name = 'point_create.html'                # Будем использовать тот же шаблон, что и для создания публикации
#     success_url = reverse_lazy('mypoints')             # Указываем, куда перенаправить пользователя после изменения поста


# class PointDelete(DeleteView):
#     model = Point
#     template_name = 'point_delete.html'
#     success_url = reverse_lazy('mypoints')             # Указываем, куда перенаправить пользователя после удаления публикации

