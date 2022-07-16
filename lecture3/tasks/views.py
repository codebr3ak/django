from django.shortcuts import render

tasks = ["Food", "Bazz", "Bar"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })