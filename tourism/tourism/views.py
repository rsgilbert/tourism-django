from django.shortcuts import render   

def uganda(request):
    return render(request, "uganda.html", {"country": "Uganda"})
