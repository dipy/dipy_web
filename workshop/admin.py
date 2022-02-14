from django.contrib import admin

from . import models
# Register your models here.


class WorkshopAdmin(admin.ModelAdmin):
    filter_horizontal = ('speakers', 'bg_images', 'members', 'pricing_tiers')


class QAAdmin(admin.ModelAdmin):
    filter_horizontal = ('panel',)

class VideoAdmin(admin.ModelAdmin):
    filter_horizontal = ('speakers', 'workshops')

admin.site.register(models.BackgroundImage)
admin.site.register(models.Speaker)
admin.site.register(models.Workshop, WorkshopAdmin)
admin.site.register(models.WorkshopEvent)
admin.site.register(models.Pricing)
admin.site.register(models.Subscription)
admin.site.register(models.Lesson)
admin.site.register(models.QA, QAAdmin)
admin.site.register(models.Video, VideoAdmin)
