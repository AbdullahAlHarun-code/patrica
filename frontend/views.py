from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse


# Create your views here.
def index(request):
    context = {
        'title':'Home page'
    }
    return render(request, "frontend/index.html", context)
