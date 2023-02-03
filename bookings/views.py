from django.shortcuts import render


# Create your views here.
def index_view(request):

    return render(request, 'index.html')


def register_view(request):

    return render(request, 'register.html')


def login_view(request):

    return render(request, 'login.html')


def resetpassword_view(request):

    return render(request, 'resetpassword.html')


def contact_view(request):

    return render(request, 'contact.html')

