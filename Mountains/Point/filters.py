# Создаем свой набор фильтров для модели Point.
# FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.
# В fields содержится словарь настройки самих фильтров. Ключами являются названия полей модели, а значениями выступают списки
# операторов фильтрации. Именно те, которые мы можем указать при составлении запроса.
# Например, Post.objects.filter(price__gt=10)
# Список операторов можно посмотреть по ссылке:	https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups
# По настройке внешнего вида фильтров и способа фильтрации см.  ниже с применением ModelChoiceFilter

from django_filters import FilterSet, ModelChoiceFilter
from .models import *
from django import forms

########################################################################################################################

class PointFilter(FilterSet):
    class Meta:
        model = Point    # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        # Ключами являются названия полей модели, а значениями выступают списки операторов
                                # фильтрации(https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups).
        fields = {
            'pereval': ['exact'],
            'status': ['exact'],
        }

# ModelChoiceFilter - это выбор модели фильтра (как он будет выглядеть)
    pereval = ModelChoiceFilter(
        field_name = 'pereval',
        queryset = Pereval.objects.all(),
        label = 'Перевал',
        empty_label = '--------------------',
        widget = forms.Select(attrs={'style': 'width: 150px; height: 25px;'}),    # задаём размеры окошка для фильтрации
    )
    status = ModelChoiceFilter(
        field_name = 'status',
        queryset = Status.objects.all(),
        label = 'Статус',
        empty_label = '--------------------',
        widget = forms.Select(attrs={'style': 'width: 150px; height: 25px;'}),    # задаём размеры окошка для фильтрации
    )

########################################################################################################################

class MypointsFilter(FilterSet):
    class Meta:
        model = Point
        fields = {
            'pereval': ['exact'],
        }

    pereval = ModelChoiceFilter(
        field_name = 'pereval',
        queryset = Pereval.objects.all(),
        label = 'Перевал',
        empty_label='--------------------',
        widget = forms.Select(attrs={'style': 'width: 150px; height: 25px;'}),    # задаём размеры окошка для фильтрации
    )

########################################################################################################################