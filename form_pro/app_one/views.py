from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app_one/page_1.html', {'text' : 'Hello App One'})