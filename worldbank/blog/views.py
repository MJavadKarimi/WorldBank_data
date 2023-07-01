from django.shortcuts import render
from django.http import HttpResponse
from .models import Indicators, Countries, Datas


def index(request):
    countries_number = Countries.objects.count()
    context = {'countries_number': countries_number}
    return render(request, 'index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
