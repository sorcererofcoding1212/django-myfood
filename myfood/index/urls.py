from django.urls import path
from . import views

app_name = "index"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.about, name="about"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('create/', views.create, name="create")
]
