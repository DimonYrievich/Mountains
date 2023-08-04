
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

########################################################################################################################

class Users(models.Model):

    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)        # Связь «один к одному» с встроенной моделью User
    email = models.EmailField(max_length=254)                          # Поле для email пользователя
    phone = models.CharField(max_length=20)                            # Поле для номера телефона пользователя
    surname = models.CharField(max_length=50)                          # Поле для фамилии пользователя
    name = models.CharField(max_length=50)                             # Поле для имени пользователя
    otchestvo = models.CharField(max_length=50, blank=True)            # Поле для отчества пользователя (необязательное,
                                                                       # может быть пустым)
    def __str__(self):
        return f'{self.user.username} {self.email} {self.phone} {self.surname} {self.name} {self.otchestvo}'

########################################################################################################################

class Pereval(models.Model):

    PE = 'Планета Земля'
    PA = 'Памиро-Алай'
    A = 'Алтай'
    NSR = 'Северо-Чуйский хребет'
    SCR = 'Южно-Чуйский хребет'
    KR = 'Катунский хребет'
    FM = 'Фанские горы'
    HR = 'Гиссарский хребет (участок западнее перевала Анзоб)'
    MMK = 'Матчинский горный узел'
    TH = 'Горный узел Такали, Туркестанский хребет'
    HA = 'Высокий Алай'
    EA = 'Кичик-Алай и Восточный Алай'
    ALA = 'Аладаглар'
    T = 'Тавр'
    S = 'Саяны'
    RL = 'Хребет Листвяга'
    IR = 'Ивановский хребет'
    MMT = 'Массив Мунгун-Тайга'
    RTS = 'Хребет Цаган-Шибэту'
    RCH = 'Хребет Чихачева (Сайлюгем)'
    SHR = 'Шапшальский хребет'
    RSA = 'Хребет Южный Алтай'
    RMA = 'Хребет Монгольский Алтай'
    WS = 'Западный Саян'
    ES = 'Восточный Саян'
    KA = 'Кузнецкий Алатау'
    KUR = 'Курайский хребет'

    POSITIONS = [
        (PE, 'Планета Земля'),
        (PA, 'Памиро-Алай'),
        (A, 'Алтай'),
        (NSR, 'Северо-Чуйский хребет'),
        (SCR, 'Южно-Чуйский хребет'),
        (KR, 'Катунский хребет'),
        (FM, 'Фанские горы'),
        (HR, 'Гиссарский хребет (участок западнее перевала Анзоб)'),
        (MMK, 'Матчинский горный узел'),
        (TH, 'Горный узел Такали, Туркестанский хребет'),
        (HA, 'Высокий Алай'),
        (EA, 'Кичик-Алай и Восточный Алай'),
        (ALA, 'Аладаглар'),
        (T, 'Тавр'),
        (S, 'Саяны'),
        (RL, 'Хребет Листвяга'),
        (IR, 'Ивановский хребет'),
        (MMT, 'Массив Мунгун-Тайга'),
        (RTS, 'Хребет Цаган-Шибэту'),
        (RCH, 'Хребет Чихачева (Сайлюгем)'),
        (SHR, 'Шапшальский хребет'),
        (RSA, 'Хребет Южный Алтай'),
        (RMA, 'Хребет Монгольский Алтай'),
        (WS, 'Западный Саян'),
        (ES, 'Восточный Саян'),
        (KA, 'Кузнецкий Алатау'),
        (KUR, 'Курайский хребет'),
    ]

    name_pereval = models.CharField(max_length=60, choices = POSITIONS, default = PE, unique = True)

    def __str__(self):
        return self.name_pereval

########################################################################################################################

class Status(models.Model):

    NEW = 'new'
    PEN = 'pending'
    ACC = 'accepted'
    REJ = 'rejected'

    POSITION = [
        (NEW, 'new'),
        (PEN, 'pending'),
        (ACC, 'accepted'),
        (REJ, 'rejected'),
    ]

    name_status = models.CharField(max_length=20, choices = POSITION, default = NEW, unique=False)

    def __str__(self):
        return self.name_status

########################################################################################################################

class Level(models.Model):

    winter = 'winter'
    summer = 'summer'
    autumn = 'autumn'
    spring = 'spring'

    SEASON = [
        (winter, 'winter'),
        (summer, 'summer'),
        (autumn, 'autumn'),
        (spring, 'spring'),
    ]

    name_level = models.CharField(max_length=20, choices = SEASON, default = winter, unique=False)

    def __str__(self):
        return self.name_level

########################################################################################################################
                                     # Таблица с географическими координатами
class Coords(models.Model):

    latitude = models.FloatField()                  # Широта
    longitude = models.FloatField()                 # Долгота
    height = models.IntegerField(default = 0)       # Высота

    def __str__(self):
        return f'Широта: {self.latitude} || Долгота: {self.longitude} || Высота: {self.height}'

########################################################################################################################

class Point(models.Model):

    pereval = models.ManyToManyField('Pereval', through = 'PointPereval', related_name='point')     # Связь с перевалами
    title = models.CharField(max_length=50)                                                         # Поле для заголовка
    description = models.TextField()                                                                 # Поле для описания
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)                # Поле с географическими координатами
    level = models.ManyToManyField('Level', through = 'PointLevel', related_name='point')   # Связь с уровнями сложности
    photo = models.ImageField(upload_to='photos/', blank=True)      # Определяем поле для вложений(фото), необязательное
    user = models.ForeignKey('Users', on_delete=models.CASCADE)                 # Связь «один ко многим» с моделью Users
    add_time = models.DateTimeField(auto_now_add=True)                                                # Время публикации
    status = models.ManyToManyField('Status', through = 'PointStatus', related_name='point')        # Связь со статусами

    # Для вывода в HTML странице указываем, как должен выглядеть объект нашей модели (что именно нужно выводить)
    def __str__(self):
        return f'{self.pereval} {self.title} {self.description[:1000]} {self.coords} {self.level} {self.photo} ' \
               f'{self.user} {self.add_time} {self.status}'

    # Добавим метод get_absolute_url, чтобы указать, какую страницу нужно открыть после создания публикации
    # Функция reverse позволяет указать не путь вида /board/…, а название пути.
    def get_absolute_url(self):
        return reverse('point_detail', args=[str(self.id)])

########################################################################################################################
                                            #Промежуточная таблица
class PointPereval(models.Model):

    point = models.ForeignKey("Point", on_delete=models.CASCADE)
    pereval = models.ForeignKey("Pereval", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.point}:{self.pereval}'

########################################################################################################################
                                           #Промежуточная таблица
class PointLevel(models.Model):

    point = models.ForeignKey("Point", on_delete=models.CASCADE)
    level = models.ForeignKey("Level", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.point}:{self.level}'

########################################################################################################################
                                           #Промежуточная таблица
class PointStatus(models.Model):

    point = models.ForeignKey("Point", on_delete=models.CASCADE)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.point}:{self.status}'

########################################################################################################################