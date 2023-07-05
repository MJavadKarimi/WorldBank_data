from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("comparison/<str:indicator>/country/<str:country1>/vs/<str:country2>/", views.comparison_data, name="comparison"),
]