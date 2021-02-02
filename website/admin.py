from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.WebsiteSection)
admin.site.register(models.NewsPost)
admin.site.register(models.Publication)
admin.site.register(models.CarouselImage)
admin.site.register(models.SponsorImage)
admin.site.register(models.DocumentationLink)
