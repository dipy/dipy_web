import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import markdown
import bleach

# markdown allowed tags that are not filtered by bleach

allowed_html_tags = bleach.ALLOWED_TAGS + ['p', 'pre', 'table', 'img',
                                           'h1', 'h2', 'h3', 'h4', 'h5',
                                           'h6', 'b', 'i', 'strong', 'em',
                                           'tt', 'br', 'blockquote',
                                           'code', 'ul', 'ol', 'li',
                                           'dd', 'dt', 'a', 'tr', 'td',
                                           'div', 'span', 'hr']

allowed_attrs = ['href', 'class', 'rel', 'alt', 'class', 'src']

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

    # determines for what purpose the article is used. Eg: index-header, body,
    # installation-page, getting-started-page etc
    website_position_id = models.CharField(max_length=100,
                                           unique=True,
                                           db_index=True)

    # fixed sections cannot be added or deleted, pages can be added or deleted
    # and pages can also be listed in the nav bar
    SECTION_TYPE_CHOICES = (
        ('fixed', 'Fixed Section'),
        ('page', 'Page'),
    )
    section_type = models.CharField(max_length=100,
                                    choices=SECTION_TYPE_CHOICES,
                                    default='page')
    show_in_nav = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ("view_section", "Can see available sections"),
            ("edit_section", "Can edit available sections"),
        )

    def save(self, *args, **kwargs):
        html_content = markdown.markdown(self.body_markdown,
                                         extensions=['codehilite'])
        print(html_content)
        # bleach is used to filter html tags like <script> for security
        self.body_html = bleach.clean(html_content, allowed_html_tags,
                                      allowed_attrs)
        self.modified = datetime.datetime.now()
        # Call the "real" save() method.
        super(WebsiteSection, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    body_markdown = models.TextField()
    body_html = models.TextField(editable=False)
    post_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        html_content = markdown.markdown(self.body_markdown,
                                         extensions=['codehilite'])
        print(html_content)
        # bleach is used to filter html tags like <script> for security
        self.body_html = bleach.clean(html_content, allowed_html_tags,
                                      allowed_attrs)
        self.modified = datetime.datetime.now()
        # Call the "real" save() method.
        super(NewsPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Publication(models.Model):
    """
    Model for storing publication information.
    """
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    doi = models.CharField(max_length=100, null=True, blank=True)
    # entry type like article, inproceedings, book etc
    entry_type = models.CharField(max_length=100, null=True, blank=True)
    # name of journal in case of article or booktitle in case of
    # inproceedings
    published_in = models.CharField(max_length=200, null=True, blank=True)
    publisher = models.CharField(max_length=200, null=True, blank=True)
    year_of_publication = models.CharField(max_length=4, null=True, blank=True)
    month_of_publication = models.CharField(max_length=10, null=True,
                                            blank=True)
    bibtex = models.TextField(null=True, blank=True)
    is_highlighted = models.BooleanField(default=False)

    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.now()
        # Call the "real" save() method.
        super(Publication, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class CarouselImage(models.Model):
    """
    Model for storing image links for carousel.
    """
    image_caption = models.CharField(max_length=200)
    image_description = models.TextField(blank=True, null=True)
    target_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(max_length=200)
    display_description = models.BooleanField(default=True)

    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.now()
        # Call the "real" save() method.
        super(CarouselImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.image_url


class HoneycombPost(models.Model):
    """
    Model for storing image links for honeycomb visualisation.
    """
    image_caption = models.CharField(max_length=200)
    image_url = models.URLField(max_length=200)
    target_url = models.URLField(max_length=200)

    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        self.modified = datetime.datetime.now()
        # Call the "real" save() method.
        super(HoneycombPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.image_url


class DocumentationLink(models.Model):
    """
    Model for storing links to the documentation pages
    """
    version = models.CharField(max_length=20, unique=True)
    url = models.URLField(max_length=100)
    displayed = models.BooleanField(default=True)
