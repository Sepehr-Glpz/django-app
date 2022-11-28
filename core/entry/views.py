from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import EntryRequest, get_request_by_email, resolve_entry, get_request_by_id, entry_repeated, convert_id
from entry.forms import RequestForm, SignupForm
from django.core.exceptions import ObjectDoesNotExist
from uuid import UUID
from django.contrib.auth import login
import logging

# Create your views here.

logger = logging.getLogger(__name__)


def invite_page(request):
    form = RequestForm()
    context = {"form": form}
    return HttpResponse(render(request, 'entry/invite_request.html', context))


def create_invite(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        form.is_valid()

        context = None
        entry_request = get_request_by_email(form.data['email'])
        if entry_repeated(entry_request):
            context = {"error": "This User has already been invited!"}
            return HttpResponse(render(request, 'entry/invite_link.html', context))

        if not form.is_valid():
            return redirect("/entry/invite")
        entry_request = form.save()

        link = create_invite_link(entry_request.id, request)
        context = {"link": link}

        return HttpResponse(render(request, 'entry/invite_link.html', context))
    return HttpResponse("Not Found")


def create_invite_link(user_id, request):
    host = request.get_host()
    return f"{host}/entry/invite/{user_id}"


def get_invite_form(request, link):
    context = None
    user_id = convert_id(link)
    if user_id is None:
        return HttpResponse(render(request, 'not_found.html', {"error": "invalid id!"}))
    try:
        requested_entry = EntryRequest.objects.get(id=link)
        if requested_entry.resolved:
            context = {"error": "This Users entry has already been resolved!"}
        else:
            entry_request, _ = get_request_by_id(user_id)
            form = SignupForm(initial={"email": entry_request.email})
            context = {"content": form, "id": user_id}
    except ObjectDoesNotExist:
        context = {"error": "Failed to find"}

    return HttpResponse(render(request, "entry/invite.html", context))


def signup(request, id):
    if request.method != "POST":
        return redirect("/entry/invite")

    context = None

    user_id = convert_id(id)
    if user_id is None:
        context = {"error": "invalid Id!"}
        return HttpResponse(render(request, 'not_found.html', context))

    user_form = SignupForm(request.POST)

    if not user_form.is_valid():
        context = {"content": user_form, "id": user_id}
        return HttpResponse(render(request, 'entry/invite.html', context))

    user_form.save()
    resolve_entry(id)

    return redirect("/management/login")


