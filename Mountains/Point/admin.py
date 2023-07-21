
from django.contrib import admin
from .models import *

#Регистрируем все созданные модели для отображения их в админке
admin.site.register(Users)
admin.site.register(Pereval)
admin.site.register(Level)
admin.site.register(Coords)
admin.site.register(Point)
admin.site.register(PointPereval)
admin.site.register(PointLevel)