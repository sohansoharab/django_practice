from django.shortcuts import render

# Create your views here.

def index(request):
    cont = {
        'text': 'Hello App Two'
    }
    return render(request, 'app_one/page_1.html', context=cont)