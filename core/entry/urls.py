from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("invite/<str:link>", views.get_invite_form, name="invite"),
    path("invite", views.create_invite, name="create_invite")
]
