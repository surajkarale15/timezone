from django.contrib import admin
from django.urls import path
from timezone_output.views import *



urlpatterns = [
    path('welcome/', welcome_timezone_page),
    path('persist/', save_or_update),
    # path("delete/<int:pid>",delete_timezone),
    # path("edit/<int:pid>",fetch_timezone)
]
