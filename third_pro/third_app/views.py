from django.shortcuts import render
from third_app.models import UserPage

# Create your views here.


def index(request):
    title = 'HOME'
    my_dict = {
        'title': title,
        'home_text': 'Go the domain/user'
    }
    return render(request, 'third_app/index.html', context=my_dict)


def user_page(request):
    mylist = UserPage.objects.order_by('frst_name')

    my_dict = {
        'title': 'Users',
        'user_info': mylist
    }
    return render(request, 'third_app/index.html', context=my_dict)
