from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework import permissions

from windcockpit.forms import SessionForm
from windcockpit.models import Session
from windcockpit.serializiers import SessionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the windcockpit index.")


def sessions(request):
    latest_session_list = Session.objects.order_by("-date")
    return render(request, "windcockpit/sessions.html", {
        "latest_session_list": latest_session_list
    })


def session(request, session_id):
    s = get_object_or_404(Session, pk=session_id)

    if request.method == "POST":
        form = SessionForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
        return redirect("windcockpit:sessions")
    else:
        form = SessionForm(instance=s)
        return render(request, "windcockpit/session.html", {"form": form})


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Session.objects.all().order_by('-date')
    serializer_class = SessionSerializer
    permission_classes = [permissions.AllowAny]
