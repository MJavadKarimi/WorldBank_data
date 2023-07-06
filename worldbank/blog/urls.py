from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("comparison/<str:indicator_id>/country/<str:country1_id>/vs/<str:country2_id>/", views.comparison_data, name="comparison"),
]