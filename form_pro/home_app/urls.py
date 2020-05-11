from django.urls import path
from app_two import views as v2
from app_one import views as v1
from home_app import views as hv


urlpatterns = [
    path('', hv.get_name, name='form_page'),
    path('index', hv.index, name= 'index'),
    path('app1', v1.index, name='app1'),
    path('app2', v2.index, name='app2'),
]
