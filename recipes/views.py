from django.shortcuts import render
from recipes.models import Recipe, Author

# Create your views here.


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


def recipe(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {'data': data})


def profile(request, id):
    data = Author.objects.get(id=id)
    return render(request, 'profile.html', {'data': data})
