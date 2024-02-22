from django.shortcuts import render

# Create your views here.
def aboutme(r):
    return render(r,'aboutme/aboutme.html')