from django.shortcuts import render, reverse, HttpResponseRedirect
from recipes.models import Recipe, Author
from recipes.forms import AddRecipeForm, AddAuthorForm


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


def add_recipe(request):

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time=data['time'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('home'))

    form = AddRecipeForm()

    return render(request, 'addrecipe.html', {"form": form})


def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('home'))

    form = AddAuthorForm
    return render(request, 'addauthor.html', {'form': form})


def recipe(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {'data': data})


def profile(request, id):
    author = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author=author)
    return render(request, 'profile.html', {'author': author, 'recipe': recipe})
