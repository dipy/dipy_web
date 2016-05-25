from django.db import models
from django.contrib.auth.models import User
import markdown
import bleach
import datetime

# markdown allowed tags that are not filtered by bleach

allowed_html_tags = bleach.ALLOWED_TAGS + ['p', 'pre', 'table', 'img',
                                           'h1', 'h2', 'h3', 'h4', 'h5',
                                           'h6', 'b', 'i', 'strong', 'em',
                                           'tt', 'br', 'blockquote',
                                           'code', 'ul', 'ol', 'li',
                                           'dd', 'dt', 'a', 'tr', 'td',
                                           'div', 'span', 'hr', 'iframe']

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

    # determines for what purpose the article is used. Eg: header, body etc.
    website_position_id = models.CharField(max_length=100,
                                           unique=True,
                                           db_index=True)

    # determines for which page the article is used. Eg: home, development.
    WEBSITE_PAGE_CHOICES = (
        ('home', 'Home'),
    )
    website_page = models.CharField(max_length=100,
                                    choices=WEBSITE_PAGE_CHOICES)

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
    post_date = models.DateTimeField(auto_now_add=True)
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
