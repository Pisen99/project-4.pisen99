from django.shortcuts import render
from django.views import generic, View


# Create your views here.
def index_view(request):

    return render(request, 'index.html')


def register_view(request):

    return render(request, 'register.html')
