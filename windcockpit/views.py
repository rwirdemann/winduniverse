from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from windcockpit.models import Session
from windcockpit.serializiers import SessionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the windcockpit index.")


def sessions(request):
    latest_session_list = Session.objects.order_by("-date")[:5]
    return render(request, "windcockpit/sessions.html", {
        "latest_session_list": latest_session_list
    })


def session(request, session_id):
    s = get_object_or_404(Session, pk=session_id)
    return render(request, "windcockpit/session.html", {"session": s})


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Session.objects.all().order_by('-date')
    serializer_class = SessionSerializer
    permission_classes = [permissions.AllowAny]
