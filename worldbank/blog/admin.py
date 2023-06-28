from django.contrib import admin
from .models import Indicators, Countries, Datas

# Register your models here.

class IndicatorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)


class DatasAdmin(admin.ModelAdmin):
    list_display = ('id', 'indicator', 'country', 'date', 'amount')
    ordering = ('id',)


admin.site.register(Indicators, IndicatorsAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Datas, DatasAdmin)
