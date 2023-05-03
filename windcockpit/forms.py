from django.forms import ModelForm

from windcockpit.models import Session


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ["sport", "spot"]
