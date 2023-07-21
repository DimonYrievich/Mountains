from django.urls import path
from .views import *						# Импортируем все созданные нами представления
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', PointsList.as_view(), name='points'),						# name='_____' - название пути
#	path('<int:pk>', PointDetail.as_view(), name='point_detail'),
#	path('I/', MypointsList.as_view(), name='mypoints'),
#	path('create/', PointCreate.as_view(), name='point_create'),
#	path('<int:pk>/update/', PointUpdate.as_view(), name='point_update'),
#	path('<int:pk>/delete/', PointDelete.as_view(), name='point_delete'),
	]

# Добавляем обработчик для медиа-файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)