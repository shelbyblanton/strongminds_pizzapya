from django.contrib import admin
from .models import Topping, Pizza

from django.db import models
from django.forms import CheckboxSelectMultiple


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Topping)
admin.site.register(Pizza)
