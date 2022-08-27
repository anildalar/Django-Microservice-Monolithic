from django.contrib import admin
from django.urls import path,include

from currency_country.views import  country



urlpatterns = [
    path('country/',country)
]
