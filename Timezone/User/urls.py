from django.contrib import admin
from django.urls import path
from User.views import *



urlpatterns = [
    path('welcome/', welcome_user_page),
    path('persist/', save_or_update),
    path("delete/<int:cid>",delete_user),
    path("edit/<int:cid>",fetch_user)
]
