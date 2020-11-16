#Django
from django.http import HttpResponse
from django.shortcuts import render,redirect

def homePageView(request):
    #return HttpResponse('Hello, World!')
    return render(request=request,template_name = "index.html")
