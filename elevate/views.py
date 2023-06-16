from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import Listing_Form
from . models  import Listing
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


# fetches or retrieves all the items in the DB
def list_all_items(request):
    all_listings = Listing.objects.all()  # shows all items available without filtering

    # all_listings = Listing.objects.filter(address='ruai') # only shows addresses from ruai

    # all_listings = Listing.objects.filter(title__contains = '1 bedroom') # filters the items based on title


    context = {
        'all_listings': all_listings
        

    }

    return render(request, 'all_listings.html', context)


# to retrieve a single lisitng by using the id field
def single_listing(request, pk):
    single_listing = Listing.objects.get(id=pk)

    context = {
        'listing':single_listing
    }

    return render(request, 'listing.html', context)

# updating our listings (UPDATE)
def listing_update(request, pk):
    listing_update =  Listing.objects.get(id=pk)  # first get the specific item you want to update

    form = Listing_Form(instance=listing_update)  # the specific instance to update is passed

    if request.method == 'POST':
        form = Listing_Form(request.POST, instance=listing_update, files=request.FILES)
        if form.is_valid:
            form.save()

            return redirect('all_listings')

    context = {
            'form': form
    }

    return render(request, 'listing_form.html', context)


def listing_delete(request, pk):
    listing_delete = Listing.objects.get(id=pk)

    listing_delete.delete()

    return redirect('all_listings')








