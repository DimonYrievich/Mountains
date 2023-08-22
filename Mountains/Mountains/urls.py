
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

########################################################################################################################

urlpatterns = [
    path('admin/', admin.site.urls),                            # admin
    path('pages/', include('django.contrib.flatpages.urls')),   # чтобы добавились ссылки на странички
    path('mountains/', include('Point.urls')),                  # чтобы все адреса из нашего приложения (Point/urls.py) подключались к главному приложению с префиксом mountains/
    path('sign/', include('sign.urls')),                        # все страницы, URL которых начинается с sign/, перенаправляем в приложение sign
    path('', include('protect.urls')),                          # перенаправление корневой страницы в приложение protect
    ]

# Добавляем обработчик для медиа-файлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

########################################################################################################################