from django.contrib import admin
from django.urls import path
from Task_Type.views import *



urlpatterns = [
    path('welcome/', welcome_tasktype_page),
    path('persist/', save_or_update),
    path("delete/<int:cid>",delete_tasktype),
    path("edit/<int:cid>",fetch_tasktype)
]
