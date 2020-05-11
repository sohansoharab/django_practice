from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<strong>Second app</strong>")

def help(request):
    hola = {
        'help_text' : 'This is a help page'
    }
    return render(request, 'scnd_app/index.html', context=hola)