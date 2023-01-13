from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def aboutus(request):
    if request.method=="GET":
        '''output=request.GET.get('output')'''
    return render(request,"aboutus.html")

    