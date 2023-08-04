
                                    # СОЗДАНИЕ ФОРМЫ ДЛЯ МОДЕЛИ И ВАЛИДАЦИЯ ДАННЫХ В ФОРМАХ
from django import forms
from .models import Point, Coords, Users, Pereval
from django.core.exceptions import ValidationError


########################################################################################################################
                                            # Форма для модели Coords
class CoordsForm(forms.ModelForm):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']
        labels = {
            'latitude': 'Широта',
            'longitude': 'Долгота',
            'height': 'Высота',
        }

########################################################################################################################
                                            # Форма для модели Point
class PointForm(forms.ModelForm):
    #coords_form = CoordsForm()
    class Meta:
        model = Point
        # Выбираем поля из модели. Если указать fields = '__all__' , то Django возьмет все поля.
        fields = [
            'pereval',
            'title',
            'description',
            #'coords',
            'level',
            'photo',
            'user',
            'status',
        ]
        # Меняем названия полей на русский
        labels = {
            'pereval': 'Перевал',
            'title': 'Заголовок',
            'description': 'Описание',
            'coords': 'Координаты',
            'level': 'Уровень',
            'photo': 'Фото',
            'user': 'Пользователь',
            'status': 'Статус',
            }
        #Меняем размеры и формы полей с использованием виджетов forms.Textarea, forms.Select, forms.TextInput и т.д.
        widgets = {
            #'pereval': forms.Select(attrs={'style': 'width: 300px; height: 25px;'}),
            'title': forms.TextInput(attrs={'style': 'width: 300px; height: 25px;'}),
            'description': forms.Textarea(attrs={'style': 'width: 300px; height: 25px;'}),
            #'coords': forms.Select(attrs={'style': 'width: 300px; height: 25px;'}),
            #'level': forms.Select(attrs={'style': 'width: 300px; height: 25px;'}),
            #'photo': forms.ClearableFileInput(attrs={'style': 'width: 300px; height: 25px;'}),
            'user': forms.Select(attrs={'style': 'width: 300px; height: 25px;'}),
            #'status': forms.Select(attrs={'style': 'width: 300px; height: 25px;'}),
            }

    def __init__(self, *args, **kwargs):
        super(PointForm, self).__init__(*args, **kwargs)
        self.fields['pereval'].empty_label = '---------- выбери из списка ----------'
        self.fields['level'].empty_label = '---------- выбери из списка ----------'
        self.fields['status'].empty_label = '---------- выбери из списка ----------'

        # # Устанавливаем виджет для поля 'status' как отключенный с фиксированным значением 'new'
        # self.fields['status'].widget.attrs['disabled'] = True
        # self.initial['status'] = 'new'  # Устанавливаем начальное значение 'new'


    # Валидация. Переопределяем метод clean в форме:
    def clean(self):
        cleaned_data = super().clean()

        # Проверяем длину поля description
        description = cleaned_data.get("description")
        if description is not None and len(description) < 5:
            raise ValidationError({
                "description": "Описание не может быть менее 5 символов."
            })

        # Проверяем, что название заголовка не совпадает с названиями перевалов из списка pereval !!!! НЕ РАБОТАЕТ !!!!
        title = cleaned_data.get("title")
        pereval = cleaned_data.get("pereval")
        if pereval and title:
            for name_pereval in pereval:
                if name_pereval == title:
                    raise ValidationError(
                        "Заголовок вашей публикации не должен быть идентичен названию перевала."
                    )

        return cleaned_data

########################################################################################################################