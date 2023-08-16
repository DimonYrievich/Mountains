
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PointFilter, MypointsFilter
from .forms import PointForm, CoordsForm

########################################################################################################################

class PointsList(ListView):              # ПРЕДСТАВЛЕНИЕ. Для отображения всех точек на всех перевалах
    model = Point                        # Указываем модель, объекты которой мы будем выводить
    template_name = 'points_list.html'   # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'points'       # Имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 4                      # ПАГИНАЦИЯ. Количество записей на web-странице + нужно внести изменения в шаблоне HTML

    # Фильтрация. Переопределяем функцию получения списка публикаций.
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PointFilter(self.request.GET, queryset)
        return self.filterset.qs.order_by('-add_time')
    # Фильтрация
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

########################################################################################################################

class MypointsList(LoginRequiredMixin, ListView):          # ПРЕДСТАВЛЕНИЕ. Для отображения СПИСКА всех своих публикаций
    model = Point
    template_name = 'mypoints_list.html'
    context_object_name = 'mypoints'
    login_url = 'login'                                 # Меняем путь к странице входа (сначала авторизация/регистрация,
                                                                                               # потом вход на страницу)
    # Фильтрация. Переопределяем функцию получения списка публикаций.
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = MypointsFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.order_by('-add_time')
    # Фильтрация
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

########################################################################################################################

class PerevalList(ListView):                                             # ПРЕДСТАВЛЕНИЕ. Для отображения всех перевалов
    model = Pereval
    template_name = 'pereval_list.html'
    context_object_name = 'pereval'

########################################################################################################################

class PointDetail(DetailView):                           # ПРЕДСТАВЛЕНИЕ Для отображения одного экземпляра таблицы из БД
    model = Point
    template_name = 'point_detail.html'
    context_object_name = 'point'

########################################################################################################################

class PointCreate(LoginRequiredMixin, CreateView):                               # ПРЕДСТАВЛЕНИЕ для создания публикации
    form_class = PointForm                                                               # Указываем разработанную форму
    model = Point
    template_name = 'point_create.html'
    success_url = reverse_lazy('mypoints')        # Указываем, куда перенаправить пользователя после создания публикации

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['coords_form'] = CoordsForm(self.request.POST)
        else:
            context['coords_form'] = CoordsForm()
        return context

    def form_valid(self, form):
        coords_form = CoordsForm(self.request.POST)
        if coords_form.is_valid():
            coords = coords_form.save()
            form.instance.coords = coords

            user_profile = Users.objects.get(user=self.request.user)  # Получаем экземпляр модели Users для текущего пользователя
            form.instance.user = user_profile                         # Присваиваем полю user по умолчанию для авторизованных user-ов
            form.instance.save()                                                       # Сохраняем объекты в базе данных

            status_new = Status.objects.get(name_status='new')                 # Устанавливаем статус "new" по умолчанию
            form.instance.status.add(status_new)                               # Устанавливаем статус "new" по умолчанию

            return super().form_valid(form)
        else:
            return self.form_invalid(form)

########################################################################################################################

class PointUpdate(UpdateView, LoginRequiredMixin):                              # ПРЕДСТАВЛЕНИЕ для изменения публикации
    form_class = PointForm                               # Будем использовать ту же форму, что и для создания публикации
    model = Point
    template_name = 'point_update.html'
    success_url = reverse_lazy('mypoints')       # Указываем, куда перенаправить пользователя после изменения публикации

########################################################################################################################

class PointDelete(DeleteView, LoginRequiredMixin):
    model = Point
    template_name = 'point_delete.html'
    success_url = reverse_lazy('mypoints')        # Указываем, куда перенаправить пользователя после удаления публикации

########################################################################################################################