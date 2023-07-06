from django.shortcuts import render
from django.http import HttpResponse
from .models import Indicators, Countries, Datas


def index(request):
    countries_number = Countries.objects.count()
    context = {'countries_number': countries_number}
    return render(request, 'index.html', context)


def comparison_data(request, indicator_id, country1_id, country2_id):
    
    indicator = Indicators.objects.values('name').get(id=indicator_id)['name']
    country1 = Countries.objects.values('name').get(id=country1_id)['name']
    country2 = Countries.objects.values('name').get(id=country2_id)['name']
    data1 = Datas.objects.values('date', 'amount').filter(indicator=indicator_id, country=country1_id)
    data2 = Datas.objects.values('date', 'amount').filter(indicator=indicator_id, country=country2_id)

    context = {
        'indicator': indicator,
        'country1': country1,
        'country2': country2,
        'data1': data1,
        'data2': data2,
        }
    return render(request, 'comparison.html', context)
