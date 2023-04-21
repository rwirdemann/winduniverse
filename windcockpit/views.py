from django.http import HttpResponse

from windcockpit.models import Session


def index(request):
    return HttpResponse("Hello, world. You're at the windcockpit index.")


def sessions(request):
    latest_session_list = Session.objects.order_by("-date")[:5]
    output = ", ".join([s.__str__() for s in latest_session_list])
    return HttpResponse(output)


def session(request, session_id):
    return HttpResponse("You're looking at session %s" % session_id)
