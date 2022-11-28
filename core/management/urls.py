from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('info/', views.get_info, name="info"),
    path('info/<str:user_id>/', views.get_user_info, name="user_info"),
    path('user/<str:user_id>', views.edit_user, name="update_user"),
]
