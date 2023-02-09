import uuid
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django_cut_url_site.settings import ALLOWED_HOSTS
from .forms import *
import requests

menu = [
    {'title': 'Cut url', 'url_name': 'home'},
    {'title': 'Registration', 'url_name': 'reg'},
    {'title': 'Authorization', 'url_name': 'auth'},
]

host = ALLOWED_HOSTS[0]
port = '8000'


def index(request):
    short_url = ''

    if request.method == 'POST':
        form = AddShortUrl(request.POST)

        if form.is_valid():
            url = request.POST['url']

            if url_is_valid(url):
                try:
                    row = ShortUrl.objects.get(url=url)
                    short_url = row.short_url
                except:
                    row = ShortUrl(url=url, short_url=generateShortUrl())
                    row.save()
                    short_url = row.short_url
            else:
                short_url = 'Invalid URL!'
    else:
        form = AddShortUrl()

    context = {
        'title': 'Cut url',
        'menu': menu,
        'form': form,
        'short_url': short_url,
    }
    return render(request, 'cut_url/index.html', context=context)


def generateShortUrl() -> str:
    token = uuid.uuid4()
    return host + ':' + port + '/' + str(token)[:8]


def url_is_valid(url: str) -> bool:
    try:
        requests.head(url)
        return True
    except:
        return False


def url_catcher(request, token: str):
    try:
        row = ShortUrl.objects.get(short_url=host + ':' + port + '/' + token)
    except:
        return Http404()
    return redirect(row.url)


def PageNotFound(request, exception):
    return HttpResponseNotFound('Page 404')
