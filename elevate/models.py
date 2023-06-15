from django.db import models


# Create your models here. which are just tables in the DB schema
class Listing(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.title                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
