from django.db import models

class Movie(models.Model):
    original_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=50)
    movie_genre = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    avg_imdb = models.FloatField()

class Review(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    original_source = models.URLField()
    review_title = models.CharField(max_length=40)
    review_text = models.TextField()