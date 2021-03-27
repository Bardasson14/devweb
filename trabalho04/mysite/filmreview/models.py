from django.db import models

class Movie(models.Model):
    
    def __str__(self):
        return self.original_title

    original_title = models.CharField(max_length=100)
    director_name = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    release_year = models.CharField(max_length=4)
    country = models.CharField(max_length=30)
    avg_imdb = models.FloatField()
    synopsis = models.TextField(default="")

class Review(models.Model):
    
    def __str__(self):
        return self.title
    
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    original_source = models.URLField()
    title = models.CharField(max_length=40)
    text = models.TextField()
    avaliation = models.FloatField(null=False)
