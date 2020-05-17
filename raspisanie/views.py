from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'user_raspisanie/raspisanie.html', {})
