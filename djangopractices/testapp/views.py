from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    res = "Hi bye"
    return HttpResponse(res)
def hii(request):
    return render(request,'templates/testapp/results.html')