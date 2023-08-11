from django.urls import path

from playground import views

urlpatterns =[
    path("welcome/", views.play),
    path("books/<int:pk>/",views.getBooks)
]