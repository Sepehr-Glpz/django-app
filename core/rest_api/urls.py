from django.urls import path, include
import rest_api.views as views
from rest_framework import routers

urlpatterns = [
    path('entry/', views.EntryRequestView.as_view()),
    path('users/', views.ManagmentUserView.as_view()),
]
