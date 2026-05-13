from django.shortcuts import render, get_object_or_404
from .models import Animal

def index(request):
    animals = Animal.objects.all()
    context = {
        'animals': animals
    }
    return render(request, 'index.html', context)

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animal_detail.html', {'animal': animal})

def healthy_animals(request):
    healthy_animals = Animal.objects.filter(
        health__in=['Отличное', 'Хорошее']
    )
    context = {'healthy_animals': healthy_animals}
    return render(request, 'healthy_animals.html', context)


