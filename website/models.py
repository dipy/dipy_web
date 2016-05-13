from django.db import models
from django.contrib.auth.models import User
import markdown
import datetime

# Create your models here.


class Profile(models.Model):
    "Stores additional information about the user"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class WebsiteSection(models.Model):
    title = models.CharField(max_length=200)
    body_markdown = models.TextField()
    body_html = models.TextField(editable=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now_add=True)

    # determines for what purpose the article is used. Eg: header, body etc.
    website_position_id = models.CharField(max_length=100,
                                           unique=True,
                                           null=True)

    class Meta:
        permissions = (
            ("view_section", "Can see available sections"),
            ("edit_section", "Can edit available sections"),
        )

    def save(self, *args, **kwargs):
        self.body_html = markdown.markdown(self.body_markdown,
                                           extensions=['codehilite'])
        self.modified = datetime.datetime.now()
        # Call the "real" save() method.
        super(WebsiteSection, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
