from django.shortcuts import render
from .models import Breed, Dog
from django.http import HttpResponseRedirect, HttpResponse
#главная страница
def main(request):
    sobaka = Dog.objects.all()
    poroda = Breed.objects.all()
    return render(request, 'index.html',{'breed': poroda, 'dog': sobaka})

def por(request, id_poroda):
    sobaka = Dog.objects.filter(breed_id=id_poroda)
    poroda = Breed.objects.all()
    return render(request, 'index.html',{'breed': poroda, 'dog': sobaka})

def d(request, id_dog):
    sobaka = Dog.objects.get(id=id_dog)
    poroda = Breed.objects.all()
    return render(request, 'info.html',{'breed': poroda, 'dog': sobaka})

def breed_list(request):
    poroda = Breed.objects.all()
    return render(request, 'list.html',{'breed': poroda})

def photo(request):
    sobaka = Dog.objects.all()
    poroda = Breed.objects.all()
    return render(request, 'photos.html',{'breed': poroda, 'dog': sobaka})

def about(request):
    poroda = Breed.objects.all()
    return render(request, 'onas.html',{'breed': poroda})

def formAddBreed(request):
    breeds = Breed.objects.all()
    return render(request, 'addBreed.html', {'breeds': breeds})

def addBreed(request):
    name = request.POST.get("title")
    newBreed = Breed()
    newBreed.title = name
    newBreed.save()
    return HttpResponseRedirect("/addbreedform/")

def formAddDog(request):
    breeds = Breed.objects.all()
    return render(request, 'addDog.html', {'breeds': breeds})

def addDog(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    weight = request.POST.get("weight")
    description = request.POST.get("desc")
    breed_id = request.POST.get("breed")
    poroda = Breed.objects.get(id=breed_id)
    photo = request.FILES['image']
    dog = Dog()
    dog.name = name
    dog.age = age
    dog.weight = weight
    dog.description = description
    dog.breed = poroda
    dog.photo = photo
    dog.save()
    return HttpResponseRedirect("/adddogform")

def formEditBreed(request, id_breed):
    breed = Breed.objects.get(id=id_breed)
    return render(request, 'updateBreed.html', {'oldName': breed, 'id': id_breed})

def formEditDog(request, id_dog):
    dog = Dog.objects.get(id=id_dog)
    all_breeds = Breed.objects.all()
    return render(request, 'updateDog.html', {
        'old': dog,
        'breeds': all_breeds,
        'id': id_dog
    })

def editBreed(request):
    id = request.POST.get("id")
    name = request.POST.get("title")
    poroda = Breed.objects.get(id=id)
    poroda.title = name
    poroda.save()
    return HttpResponseRedirect("/editbreedform/" + id)

def deleteBreed(request, id_breed):
    poroda = Breed.objects.get(id=id_breed)
    poroda.delete()
    return HttpResponse('<h1>Порода успешно удалена</h1><br><a href="/">На главную</a>')

def deleteDog(request, id_dog):
    dog = Dog.objects.get(id=id_dog)
    dog.delete()
    return HttpResponse('<h1>Собака успешно удалена</h1><br><a href="/">На главную</a>')

def editDog(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    age = request.POST.get("age")
    weight = request.POST.get("weight")
    description = request.POST.get("desc")
    breed_id = request.POST.get("breed")
    breed = Breed.objects.get(id=breed_id)
    photo = None
    if 'image' in request.FILES:
        photo = request.FILES['image']
    dog = Dog.objects.get(id=id)
    dog.name = name
    dog.age = age
    dog.weight = weight
    dog.description = description
    dog.breed = breed
    if photo != None:
        dog.photo = photo
    dog.save()
    return HttpResponseRedirect("/editdogform/"+id)