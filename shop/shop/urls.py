from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('breed/<int:id_poroda>', views.por),
    path('dog/<int:id_dog>', views.d),
    path('list', views.breed_list),
    path('photos', views.photo),
    path('onas', views.about),
    path('addbreed/', views.addBreed),
    path('addbreedform/', views.formAddBreed),
    path('adddogform/', views.formAddDog),
    path('adddog/', views.addDog),
    path('deletebreed/<int:id_breed>', views.deleteBreed),
    path('editbreedform/<int:id_breed>', views.formEditBreed),
    path('editdogform/<int:id_dog>', views.formEditDog),
    path('editdog/', views.editDog),
    path('editbreed/', views.editBreed),
    path('deletedog/<int:id_dog>', views.deleteDog),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)