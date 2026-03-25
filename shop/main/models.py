from django.db import models

# порода собаки
class Breed(models.Model):
    title = models.CharField(max_length = 1000, unique = True)
    # функция для преобразования в строку
    def __str__(self):
        return self.title

# собака
class Dog(models.Model):
    name = models.CharField(max_length = 500)
    age = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)

    def str(self):
        return f'{self.name} ({self.breed.title})'