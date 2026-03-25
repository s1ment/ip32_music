from django.shortcuts import render, redirect
from .models import Genres
from .models import Track
from .forms import GenreForm
def index (request):
    genres1 = Genres.objects.all
    return render (request, 'index.html', {'genres1': genres1})

def genres (request):
    genres1 = Genres.objects.all
    return render (request, 'genres.html', {'genres1': genres1})

def track(request):
    track1 = Track.objects.all()
    return render (request, 'track.html', {'track1': track1})

def add_genre(request):
    if request.method == "POST":  

        genre = GenreForm(request.POST)
        if genre.is_valid():  
            genre.save()  
            return redirect("/genres")  
    else:
        genreform = GenreForm()  
    return render(request, "add_genre.html", {"form": genreform})

def delete_genre(request, id_genre):
    genre = Genres.objects.get(id=id_genre)
    genre.delete()
   

def edit_genre(request, id_genre):
    g = Genres.objects.get(id=id_genre)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=g)
        if form.is_valid():
            form.save()
            return redirect("/genres")
    else:
        form = GenreForm(instance=g)
    return render(request, "edit_genre.html", {"form": form})