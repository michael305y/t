from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_page(request):
    context = {

    }
    return render(request, 'Homepage.html', )


    return HttpResponse('Niaje')