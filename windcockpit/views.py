from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from rest_framework import permissions
from windcockpit.models import Session
from windcockpit.serializiers import SessionSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the windcockpit index.")


def sessions(request):
    latest_session_list = Session.objects.order_by("-date")[:5]
    template = loader.get_template("windcockpit/sessions.html")
    context = {
        "latest_session_list": latest_session_list
    }
    return HttpResponse(template.render(context, request))


def session(request, session_id):
    return HttpResponse("You're looking at session %s" % session_id)


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Session.objects.all().order_by('-date')
    serializer_class = SessionSerializer
    permission_classes = [permissions.AllowAny]
