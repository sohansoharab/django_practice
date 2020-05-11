from django.urls import path
from frst_app import views

urlpatterns = [
    path('', views.hello, name='index'),
    path('dui', views.hello, name='hello'),
    path('dui/s', views.index, name='index'),
]