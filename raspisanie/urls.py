from django.urls import path
from . import views


urlpatterns = [
path('', views.group_select, name='home'),
path('view_raspis/<int:pk>/', views.view_raspis, name='view_raspis'),
]
