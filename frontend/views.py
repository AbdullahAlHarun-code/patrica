from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse


# Create your views here.
def index(request):
    print('hello mama')
    return HttpResponse('hello mmama kemon aso? ami valo asi')
git push -u origin main
