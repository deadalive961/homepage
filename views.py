from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Daniel + Gina = FriendZone</h1>")
