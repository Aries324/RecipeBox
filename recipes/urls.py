
from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
    path('recipe/<int:id>/', views.recipe),
    path('profile/<int:id>/', views.profile)
]
