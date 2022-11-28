from django.urls import path
from . import views

urlpatterns = [
    path('invite', views.invite_page, name="invite"),  # begin entry request
    path('invite/create', views.create_invite, name="create_invite"),  # create request
    path("invite/<str:link>", views.get_invite_form, name="invite_form"),  # fill out request
    path('invite/signup/<str:id>', views.signup, name="signup")  # finish request
]
