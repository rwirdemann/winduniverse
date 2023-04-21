from django.contrib import admin

# Register your models here.
from .models import Session, Spot

admin.site.register(Session)
admin.site.register(Spot)
