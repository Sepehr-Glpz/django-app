from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import EntryRequest, get_request_by_email, resolve_entry, get_request_by_id
from entry.forms import RequestForm, SignupForm
from django.core.exceptions import ObjectDoesNotExist
from uuid import UUID
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

        if not form.is_valid():
            return redirect("invite/")

        form.save()
        user, err = get_request_by_email(form.cleaned_data['email'])

        context = None
        if err is not None:
            context = {"error": err}
        else:
            link = create_invite_link(user.id, request)
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
        return HttpResponse(render(request, 'not_found.html',{"error": "invalid id!"}))
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
        redirect("/invite/")

    pass_valid = validate_password(user_form.cleaned_data)
    if not pass_valid:
        context = {"content": user_form, "id": user_id}
        return HttpResponse(render(request, 'entry/invite.html', context))

    user_form.save()
    resolve_entry(id)

    return HttpResponse(render(request, 'entry/welcome.html', context))


def convert_id(user_id):
    try:
        uuid_obj = UUID(user_id, version=4)
        return uuid_obj
    except ValueError:
        return None


def validate_password(data_dict):
    password = data_dict["password"]
    confirmation = data_dict["confirm_password"]
    if password != confirmation:
        return False
    return True