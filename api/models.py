from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_rating(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)

        if len(ratings) == 0:
            return 0

        for rating in ratings:
            sum += rating.stars
        return sum / len(ratings)

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # if movie is removed, remove rating as well
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user is prebuild model in django
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)  # makes unique according to these combinations
        index_together = (('user', 'movie'),)
