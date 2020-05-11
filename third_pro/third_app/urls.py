from django.urls import path,include
from third_app import views

urlpatterns = [
    path('', views.user_page, name='user'),
]
