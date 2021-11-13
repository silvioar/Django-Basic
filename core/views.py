from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
        
from django.shortcuts import render
from django.template import RequestContext
###########
def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response

def handler5000(request, exception=None):
    context = {}
    response = render(request, "505.html", context=context)
    response.status_code = 500
    return response