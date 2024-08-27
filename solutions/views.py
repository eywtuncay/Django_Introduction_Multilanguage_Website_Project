from django.shortcuts import render
from .models import Solutions, Services

def home(request):
    data = {
        "hizmetler": Services.objects.all(),
        "cozumler": Solutions.objects.all()
    }
    return render(request, "index.html",data)


def solutions(request):
    data = {
        "hizmetler": Services.objects.all(),
        "cozumler": Solutions.objects.all()
    }
    return render(request, "solutions.html",data)


def solutionsdetails(request, id):
    data = {
        "solution": Solutions.objects.get(id=id)
    }
    return render(request, "details.html",data)

def about(request):
    return render(request, "about.html")

def policies(request):
    return render(request, "policies.html")

def missionAndVision(request):
    return render(request, "missionAndVision.html")
