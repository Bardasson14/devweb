from django.shortcuts import render
from filmreview.models import Movie, Review

# Create your views here.
def index(request):
    highlights = Movie.objects.order_by('-id')[:2]
    print(highlights)
    previous_reviews = Movie.objects.all()[:len(Movie.objects.all())-2]
    print(previous_reviews)
    context = {'highlights': highlights, 'previous_reviews': previous_reviews}
    return render(request, 'index.html', context)

def review(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    review = Review.objects.get(movie_id=movie_id)
    context = {'movie': movie, 'review': review}
    return render(request, 'review.html', context)