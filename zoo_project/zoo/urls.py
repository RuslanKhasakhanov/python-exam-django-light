from django.urls import path
from . import views

app_name = 'zoo'

urlpatterns = [
    path('', views.index, name='index'),
    path('healthy_animals/', views.healthy_animals, name='healthy_animals'),  # исправлено
]
