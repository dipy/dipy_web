from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Speakers)
admin.site.register(models.Workshop)
admin.site.register(models.Pricing)