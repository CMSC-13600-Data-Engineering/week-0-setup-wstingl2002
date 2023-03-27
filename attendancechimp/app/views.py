from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    bio = "My name is William Stingl a UChicago student in data engineering."
    dictionary = {'bio': bio}
    return render(request, 'app/index.html', dictionary)