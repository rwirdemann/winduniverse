from django.forms import ModelForm

from windcockpit.models import Session
from windcockpit.widgets import DatePickerInput


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = ["sport", "spot", "date"]
        widgets = {
            "date": DatePickerInput()
        }
