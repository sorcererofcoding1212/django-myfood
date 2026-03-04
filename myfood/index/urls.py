from django.urls import path
from . import views

app_name = "index"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.ItemDetail.as_view(), name="about"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('create/', views.CreateItem.as_view(), name="create")
]
