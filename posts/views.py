from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseNotFound
from posts.models import *
from django.urls import reverse

def homepage(request: HttpRequest)->HttpResponse:
    ctx = {
        'object_list': Post.objects.all(),
    }
    return render(request, 'homepage.html',  ctx)


def list_detail_view(request: HttpRequest, p_slug)->HttpResponse:
    try:
        ctx = {'object_slug': Post.objects.get(slug=p_slug)}
    except Post.DoesNotExist:
        raise Http404('not found')
    return render(request, 'blogpost.html', ctx)

