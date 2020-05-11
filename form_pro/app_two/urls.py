from django.urls import path
from app_two import views as v2


urlpatterns = [
    path('', v2.index, name='app_2_page'),
]
