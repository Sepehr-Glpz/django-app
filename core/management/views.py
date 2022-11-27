from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DisplayForm
from .models import get_user_by_id

# Create your views here.

def home(request):
    return HttpResponse(render(request, "management/home.html"))

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
def edit_info(request):
    if request.method == "POST":


