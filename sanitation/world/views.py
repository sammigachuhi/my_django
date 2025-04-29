from django.shortcuts import render

# Create your views here.
def dysentry(request):
    return render(request, "world/dysentry.html", {})


