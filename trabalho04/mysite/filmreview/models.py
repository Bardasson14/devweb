from django.db import models

class Movie(models.Model):
    
    def __str__(self):
        return self.original_name

    original_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=50)
    movie_genre = models.CharField(max_length=20)
    release_year = models.CharField(max_length=4)
    country = models.CharField(max_length=30)
    avg_imdb = models.FloatField()
    sinopsis = models.TextField()

class Review(models.Model):
    
    def __str__(self):
        return self.review_title
    
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    original_source = models.URLField()
    review_title = models.CharField(max_length=40)
    review_text = models.TextField()
    avaliation = models.FloatField()
