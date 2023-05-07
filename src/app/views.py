from django.http import HttpResponse


def index(request):
    return HttpResponse("This is index page")

def index2(request):
    return HttpResponse("this is page2")

def index3(request):
    return HttpResponse("This is page 3")

def index4(request):
    return HttpResponse("I hope thi page asfasfsadfads up")