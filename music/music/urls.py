from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index', views.index),
    path('genres/', views.genres),
    path('track/', views.track),
    path('add_genre/', views.add_genre),
    path('editgenre/<int:id_genre>', views.edit_genre),
    path('artists/', views.artists, name='artists'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)