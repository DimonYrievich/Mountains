
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),                            # admin
    path('pages/', include('django.contrib.flatpages.urls')),   # чтобы добавились ссылки на странички
    path('mountains/', include('Point.urls')),                  # чтобы все адреса из нашего приложения (Point/urls.py) подключались к главному приложению с префиксом mountains/
    path('sign/', include('sign.urls')),                        # все страницы, URL которых начинается с sign/, перенаправляем в приложение sign
    path('', include('protect.urls')),                          # перенаправление корневой страницы в приложение protect
    ]