from django.urls import path
from . import views


urlpatterns = [
path('', views.group_select, name='home'),
path('view_raspis/<int:pk>/', views.view_raspis, name='view_raspis'),
path('view_changes/<str:gruppa>', views.view_changes, name='view_changes'),
path('raspis_tomorrow/<int:pk>', views.raspis_tom, name='raspis_tomorrow'),
path('raspis_today/<int:pk>', views.raspis_today, name='raspis_today'),
]
