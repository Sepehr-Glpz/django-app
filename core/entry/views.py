from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import EntryRequest, get_request_by_email
from entry.forms import RequestForm, SignupForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def invite_page(request):
    form = RequestForm()
    context = {"form": form}
    return HttpResponse(render(request, 'entry/invite_request.html', context))


def create_invite(request):
    if request.method == "POST":
        form = RequestForm(request.POST)

        if not form.is_valid():
            return redirect("/invite/")

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
    try:
        requested_entry = EntryRequest.objects.get(id=link)
        if requested_entry.resolved:
            context = {"error": "This Users entry has already been resolved!"}
        else:
            form = SignupForm()
            context = {"content": form}
    except ObjectDoesNotExist:
        context = {"error": "Failed to find"}

    return HttpResponse(render(request, "entry/invite.html", context))

