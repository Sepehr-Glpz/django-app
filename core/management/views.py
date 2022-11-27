from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DisplayForm
from .models import get_user_by_id, is_normal_user, get_all_users

# Create your views here.

@login_required
def home(request):
    users = get_all_users()
    context = {"users": users, "current_id": request.user.id}
    return HttpResponse(render(request, "management/home.html", context))

@login_required
def get_info(request):
    user = get_user_by_id(request.user.id)
    if user is None:
        return HttpResponse(render(request, 'not_found.html'))

    access_level = user.access_level.id
    form = DisplayForm(access_level, user)
    context = {"form": form, "level": access_level}
    return HttpResponse(render(request,'management/info.html', context))

@login_required
def get_user_info(request, user_id):
    current_user = get_user_by_id(request.user.id)
    if current_user is None:
        return HttpResponse(render(request, 'not_found.html'))

    current_access_level = current_user.access_level.id
    if is_normal_user(current_access_level):
        return redirect('/management/home')

    user = get_user_by_id(user_id)
    if user is None:
        return HttpResponse(render(request, 'not_found.html'))

    form = DisplayForm(current_access_level, user)
    context = {"form": form, "level": current_access_level}
    return HttpResponse(render(request, 'management/user_info.html', context))


