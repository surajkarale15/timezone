from django.contrib import admin
from django.urls import path
from Country.views import *



urlpatterns = [
    path('welcome/', welcome_country_page),
    path('persist/', save_or_update),
    path("delete/<int:cid>",delete_country),
    path("edit/<int:cid>",fetch_country)
]
