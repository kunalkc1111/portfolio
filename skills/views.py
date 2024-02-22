from django.shortcuts import render

# Create your views here.
def skills(r):
    return render(r,'skills/skills.html')