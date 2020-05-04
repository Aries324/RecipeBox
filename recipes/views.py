from django.shortcuts import render
from recipes.models import Recipe, Author

# Create your views here.


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


def recipe(request):
    data = Recipe.objects.all()
    return render(request, 'recipe.html', {'data': data})


def profile(request):
    data = Recipe.objects.all()
    return render(request, 'profile.html', {'data': data})


def profile2(request):
    data = Recipe.objects.all()
    return render(request, 'profile2.html', {'data': data})


def recipe2(request):
    data = Recipe.objects.all()
    return render(request, 'recipe2.html', {'data': data})
