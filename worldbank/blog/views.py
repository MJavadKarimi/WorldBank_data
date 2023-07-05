from django.shortcuts import render
from django.http import HttpResponse
from .models import Indicators, Countries, Datas


def index(request):
    countries_number = Countries.objects.count()
    context = {'countries_number': countries_number}
    return render(request, 'index.html', context)


def comparison_data(request, indicator, country1, country2):
    
    indicator = Indicators.objects.values('name').filter(id=indicator)
    country1 = Countries.objects.values('name').filter(id=country1)
    country2 = Countries.objects.values('name').filter(id=country2)
    data1 = Datas.objects.values('date', 'amount').filter(indicator=indicator, country=country1)
    data2 = Datas.objects.values('date', 'amount').filter(indicator=indicator, country=country2)

    context = {
        'indicator': indicator,
        'country1': country1,
        'country2': country2,
        'date1': data1,
        'date2': data2,
        }
    return render(request, 'comparison.html', context)
