
from django.urls import path
from .views import *

########################################################################################################################

urlpatterns = [
	path('', PointsList.as_view(), name='points'),						# name='_____' - название пути
	path('<int:pk>', PointDetail.as_view(), name='point_detail'),
	path('I/', MypointsList.as_view(), name='mypoints'),
	path('pereval/', PerevalList.as_view(), name='pereval'),
	path('create/', PointCreate.as_view(), name='point_create'),
	path('<int:pk>/update/', PointUpdate.as_view(), name='point_update'),
	path('<int:pk>/delete/', PointDelete.as_view(), name='point_delete'),
	]

########################################################################################################################