from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import EntryRequest
from entry.forms import RequestForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    return HttpResponse(render(request, "entry/index.html"))


def create_invite(request):
    form = RequestForm()
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/entry/invite")
    context = {"form": form}
    return HttpResponse(render(request, 'entry/invite_request.html', context))


def get_invite_form(request, link):
    requestedEntry = None
    context = None
    try:
        requestedEntry = EntryRequest.objects.get(id=link)
        if requestedEntry.resolved == True:
            context = {"error": "This Users entry has already been resolved!"}
        else:
            context = {"content": requestedEntry.email}
    except ObjectDoesNotExist:
        context = {"error": "Failed to find"}

    return HttpResponse(render(request, "entry/invite.html", context))

