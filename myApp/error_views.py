from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext



def page_not_found_404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response

def server_error_500(request):
    context = {}
    response = render(request, "500.html", context=context)
    response.status_code = 500
    return response
