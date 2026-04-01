from django.shortcuts import render, redirect, get_object_or_404
from .models import Genres
from .models import Track, Artist
from .forms import GenreForm, ArtistForm

def index (request):
    genres1 = Genres.objects.all
    return render (request, 'index.html', {'genres1': genres1})

def genres (request):
    genres1 = Genres.objects.all
    return render (request, 'genres.html', {'genres1': genres1})

def track(request):
    track1 = Track.objects.all()
    return render (request, 'track.html', {'track1': track1})

def artists(request):
    a = Artist.objects.all()
    return render(request, 'artists.html', {'artists': a})

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

def track(request):
    artists = Artist.objects.all()
    tracks = Track.objects.all()
    selected_artist = None
    if request.method == "POST":
        artist_id = request.POST.get('artist')
        if artist_id:
            try:
                selected_artist = Artist.objects.get(id=artist_id)
                tracks = Track.objects.filter(artist=selected_artist)
            except Artist.DoesNotExist:
                tracks = Track.objects.none()
    context = {
        'track1': tracks,
        'artists': artists,
        'selected_artist': selected_artist,
    }
    return render(request, 'track.html', context)

def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artists')
    else:
        form = ArtistForm()
    return render(request, 'add_artist.html', {'form': form})

def edit_artist(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artists')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'edit_artist.html', {'form': form, 'artist': artist})

def delete_artist(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == "POST":
        artist.delete()
        return redirect('artists')
    return render(request, 'delete_artist.html', {'artist': artist})