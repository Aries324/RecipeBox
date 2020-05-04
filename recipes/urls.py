
from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index),
    path('recipe', views.recipe, name='recipe'),
    path('profile', views.profile, name='profile'),
    path('recipe2', views.recipe2, name='recipe2'),
    path('profile2', views.profile2, name='profile2')
]
