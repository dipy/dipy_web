from django.contrib import admin

from . import models
# Register your models here.


class WorkshopAdmin(admin.ModelAdmin):
    filter_horizontal = ('speakers', 'bg_images', )


admin.site.register(models.BackgroundImage)
admin.site.register(models.Speaker)
admin.site.register(models.Workshop, WorkshopAdmin)
admin.site.register(models.Pricing)
