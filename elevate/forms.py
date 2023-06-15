from django.forms import ModelForm
from .models import Listing


# creating a form from our existing model/table
class Listing_Form(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'price',
            'number_of_bedrooms',
            'number_of_bathrooms',
            'square_footage',
            'address',
            'image',
            ]