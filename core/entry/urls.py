from django.urls import path
from . import views

urlpatterns = [
    path("invite/<str:link>", views.get_invite_form, name="invite"),
    # path("invite", views.invite_link, name="create_invite"),
    path('invite/create/', views.create_invite, name="create_invite"),
    path('invite', views.invite_page, name="invite")
]
