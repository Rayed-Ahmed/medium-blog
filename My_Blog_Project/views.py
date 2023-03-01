from django.shortcuts import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))
