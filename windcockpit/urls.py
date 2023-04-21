from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sessions/", views.sessions, name="sessions"),
    path("session/<int:session_id>/", views.session, name="session")
]