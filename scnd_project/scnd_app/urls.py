from django.urls import path
from scnd_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help_page', views.help, name='help')
]