from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    population = models.IntegerField()
    image_url = models.TextField()
    def __str__(self):
        return self.name

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    opening_hours = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    image_url = models.TextField()
    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateField()
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'Review for {self.attraction.name} with rating {self.rating}'