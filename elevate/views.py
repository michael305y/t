from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import Listing_Form
# Create your views here.
def show_page(request):
    context = {

    }
    return render(request, 'Homepage.html', )


    return HttpResponse('Niaje')


# view to handle form submission(CREATE)
def listing_form(request):
    form = Listing_Form()   # generates an empty form by default as the client makes a request(GET)

    if request.method == "POST":
      form = Listing_Form(request.POST,request.FILES)  # this ensures the form is populated with the filled data if the request is POST
      if form.is_valid:
          form.save()

          return redirect('all_listings')
      

    context = {
        'form': form
    }

    return render(request, 'listing_form.html', context)
