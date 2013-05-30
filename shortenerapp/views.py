from django.views.generic import ListView
from shortenerapp.models import Url
import random
import string
from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse


def index(request):
    link = "soda/"

    if request.method == 'POST':
        #salva nova url
        url_original = request.POST['url_original']
        url = Url()
        url.url_original = url_original
        url.url_modificada = link + modifica_url(url_original)
        url.save()
       
    #exibe as urls
    urls = Url.objects.order_by('-id')

    t = loader.get_template('index.html')
    c = Context({
        'Urls': urls,
    }) 
    return  HttpResponse(t.render(c))


def modifica_url(url):
    url_modificada = palavra_aleatoria()
    return url_modificada

def palavra_aleatoria():
    palavra = ""
    for i in range(6):
        palavra += random.choice(string.letters)

    return  palavra