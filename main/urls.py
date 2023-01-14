from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('info', views.info, name='info'),
    path('geography', views.geography, name='geography'),
    path('vacancies', views.vacancies, name='vacancies'),
    path('skills', views.skills, name='skills'),
]
