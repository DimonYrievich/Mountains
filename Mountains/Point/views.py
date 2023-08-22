
                # ПРЕДСТАВЛЕНИЯ (Вьюхи). Определяют, какая информация будет отображаться на веб-страницах

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PointFilter, MypointsFilter
from .forms import PointForm, CoordsForm

########################################################################################################################

class PointsList(ListView):              # Для отображения всех точек на всех перевалах
    model = Point                        # Указываем модель, объекты которой мы будем выводить
    template_name = 'points_list.html'   # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    context_object_name = 'points'       # Имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 4                      # ПАГИНАЦИЯ. Количество записей на web-странице + нужно внести изменения в шаблоне HTML

    # Переопределяем функцию получения списка публикаций.
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

class MypointsList(LoginRequiredMixin, ListView):                         # Для отображения СПИСКА всех своих публикаций
    model = Point
    template_name = 'mypoints_list.html'
    context_object_name = 'mypoints'
    login_url = 'login'                                 # Меняем путь к странице входа (сначала авторизация/регистрация,
    paginate_by = 4                                                                            # потом вход на страницу)

    # Переопределяем функцию получения списка публикаций.
    def get_queryset(self):
        queryset = super().get_queryset()                           # Получаем исходный набор всех объектов модели Point
        user = self.request.user                                        # Получаем текущего авторизованного пользователя
            # Далее фильтруем набор объектов Point по полю user, которое связано с моделью Users. Используем связь через
            # user__user, где первый user - поле в модели Point, а второй user - поле в связанной модели Users.
        filtered_queryset = queryset.filter(user__user=user)
            # Далее создаем объект MypointsFilter, передаём в него параметры фильтрации из GET-запроса и отфильтрованный
        self.filterset = MypointsFilter(self.request.GET, queryset=filtered_queryset)                   # набор queryset
        return self.filterset.qs.order_by('-add_time')

    # Фильтрация
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

########################################################################################################################

class PerevalList(ListView):                                                            # Для отображения всех перевалов
    model = Pereval
    template_name = 'pereval_list.html'
    context_object_name = 'pereval'

########################################################################################################################

class PointDetail(DetailView):                                         # Для отображения одного экземпляра таблицы из БД
    model = Point
    template_name = 'point_detail.html'
    context_object_name = 'point'

########################################################################################################################

class PointCreate(LoginRequiredMixin, CreateView):                                             # Для создания публикации
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

class PointUpdate(UpdateView, LoginRequiredMixin):                                            # Для изменения публикации
    form_class = PointForm                               # Будем использовать ту же форму, что и для создания публикации
    model = Point
    template_name = 'point_update.html'
    success_url = reverse_lazy('mypoints')       # Указываем, куда перенаправить пользователя после изменения публикации

    # Проверяем данные на валидность, сохраняем или обновляем координаты
    def form_valid(self, form):
        coords_form = CoordsForm(self.request.POST, instance=form.instance.coords)
        if coords_form.is_valid():
            coords = coords_form.save()
            form.instance.coords = coords
        return super().form_valid(form)

    # Делаем так, чтобы при статусе отличным от 'new' пользователь не мог редактировать свою публикацию
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_new_status'] = self.object.status.filter(name_status='new').exists()

        # Проверяем, есть ли у публикации координаты, и если есть, передаем их в форму CoordsForm
        if self.object.coords:
            context['coords_form'] = CoordsForm(instance=self.object.coords)
        else:
            context['coords_form'] = CoordsForm()

        return context

########################################################################################################################

class PointDelete(DeleteView, LoginRequiredMixin):                                             # Для удаления публикации
    model = Point
    template_name = 'point_delete.html'
    success_url = reverse_lazy('mypoints')        # Указываем, куда перенаправить пользователя после удаления публикации

########################################################################################################################