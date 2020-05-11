from django.shortcuts import render
from django.http import HttpResponse
from frst_app.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
    wbpg_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records': wbpg_list
    }
    return render(request, 'frst_app/index.html', context=date_dict)

def hello(request):
    my_dict = {
        'text': 'This is a text from HELLOOOOOOOOOO function'
    }
    return render(request, 'frst_app/index.html', context=my_dict)