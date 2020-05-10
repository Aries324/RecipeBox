from django.shortcuts import render, reverse, HttpResponseRedirect
from recipes.models import Recipe, Author
from recipes.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})


@login_required
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


@login_required
def add_author(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(
                    username=data["username"],
                    password=data['password']
                )
                Author.objects.create(
                    name=data['name'],
                    bio=data['bio'],
                    user=user
                )
                return HttpResponseRedirect(reverse('home'))
        form = AddAuthorForm
        return render(request, 'addauthor.html', {'form': form})
    else:
        return render(request, 'error.html')


def recipe(request, id):
    data = Recipe.objects.get(id=id)
    return render(request, 'recipe.html', {'data': data})


def profile(request, id):
    author = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author=author)
    return render(request, 'profile.html', {'author': author, 'recipe': recipe})
