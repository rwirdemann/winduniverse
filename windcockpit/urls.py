from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sessions', views.SessionViewSet)

app_name = "windcockpit"
urlpatterns = [
    path("", views.index, name="index"),
    path("sessions/", views.sessions, name="sessions"),
    path("sessions/<int:session_id>/", views.session, name="session"),
    path("sessions/<int:session_id>/", views.update_session, name="update_session"),

    path('api/', include(router.urls)),
]
