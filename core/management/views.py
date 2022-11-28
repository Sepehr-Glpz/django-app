from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DisplayForm
from .models import get_user_by_id, is_normal_user, get_all_users, get_user_access_level

# Create your views here.


@login_required(login_url='/management/login')
def home(request):
    current_user = request.user
    users = get_all_users()
    current_access_level = get_user_access_level(current_user.id)
    if current_access_level is None:
        return HttpResponse(render(request, 'not_found.html'))

    context = {"users": users, "current_id": request.user.id, "level_name": current_access_level.name}
    return HttpResponse(render(request, "management/home.html", context))


@login_required(login_url='/management/login')
def get_info(request):
    user = get_user_by_id(request.user.id)
    if user is None:
        return HttpResponse(render(request, 'not_found.html'))

    access_level = user.access_level.id
    form = DisplayForm(access_level, instance=user)
    context = {"form": form, "level": access_level, "id": user.id}
    return HttpResponse(render(request,'management/info.html', context))


@login_required(login_url='/management/login')
def get_user_info(request, user_id):
    current_user = get_user_by_id(request.user.id)
    if current_user is None:
        return HttpResponse(render(request, 'not_found.html'))

    current_access_level = current_user.access_level.id
    if is_normal_user(current_access_level):
        context = {"error": "You do not have a high enough access level!"}
        return redirect("/management/home")

    user = get_user_by_id(user_id)
    if user is None:
        return HttpResponse(render(request, 'not_found.html'))

    form = DisplayForm(current_access_level, instance=user)
    context = {"form": form, "level": current_access_level, "id": user.id}
    return HttpResponse(render(request, 'management/user_info.html', context))


@login_required(login_url='/management/login')
def edit_user(request, user_id):
    current_user = get_user_by_id(request.user.id)
    if current_user is None:
        return HttpResponse(render(request, 'not_found.html'))

    user = get_user_by_id(user_id)
    if user is None:
        return HttpResponse(render(request, 'not_found.html'))

    context = None
    if request.method == "POST":
        form = DisplayForm(current_user.access_level.id, data=request.POST, instance=user)
        if not form.is_valid():
            context = {"messages": ["failed to update user!"], "success": False}
            return HttpResponse(render(request, 'management/user_updated.html', context))

        form.save()

        context = {"messages": ["user updated successfully!"], "success": True}
        return HttpResponse(render(request, 'management/user_updated.html', context))




