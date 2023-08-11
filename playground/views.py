from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
users = [
    {"name": "sheriff"},
    {"name": "Ned"},
    {"name": "Eniola"}

]


def play(request):
    return render(request, "playground/play.html", {"Students": list(users)})


def getBooks(request,pk):
    return HttpResponse(pk)