"""Workshop Model definitions."""

__all__ = ['Speaker', 'Workshop', 'BackgroundImage', 'WorkshopEvent',
           'Lesson', 'Video', 'QA']

from django.conf import settings
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

import markdown
import bleach

from website.models import allowed_html_tags, allowed_attrs


User = get_user_model()


def generate_unique_slug(instance, new_slug=None):
    slug = new_slug or instance.name
    unique_slug = slugify(slug)
    # Klass = instance.__class__
    num = 1
    while instance.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(unique_slug, num)
        num += 1
    return unique_slug


class BackgroundImage(models.Model):
    """
    Model for storing background image in index.html or commingsoon.html.
    """
    image = models.ImageField(upload_to='bg_images/', blank=True,
                              default=f"{settings.STATIC_URL}/workshop/images/dipy_odf_vs_2018-10-03.png",
                              help_text="upload image to the server. If external_image_url is empty, this image is selected")
    external_image_url = models.URLField(max_length=300, blank=True, default='',
                                         help_text='Preferred option. define avatar url.')
    image_caption = models.CharField(max_length=200, default=None,
                                     help_text="Use for alt_text", blank=False)
    image_description = models.TextField(blank=True)
    position = models.PositiveSmallIntegerField(default=0,
                                                help_text="Background Image "
                                                        "are ordered by "
                                                        "position level. the "
                                                        "lowest priority is "
                                                        "displayed first")

    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        ordering = ['position']

    def save(self, *args, **kwargs):
        self.modified = timezone.now()

        # clear the cache
        cache.clear()

        # Call the "real" save() method.
        super(BackgroundImage, self).save(*args, **kwargs)

    @property
    def url(self):
        return self.external_image_url or self.image.url


    def __str__(self):
        return self.image_caption


class Speaker(models.Model):
    fullname = models.CharField(max_length=300)
    title = models.CharField(max_length=300, blank=True)
    affiliation = models.CharField(max_length=300, blank=True)
    avatar = models.ImageField(upload_to='speaker_images/', blank=True,
                               help_text='upload and define profile picture. We recommend using external_avatar_url instead')
    external_avatar_url = models.URLField(max_length=300, blank=True, default='',
                                          help_text='Preferred option. define avatar url.')
    position = models.PositiveSmallIntegerField(default=0,
                                                help_text="Speakers are "
                                                          "ordered by position"
                                                          " level. the lowest"
                                                          "priority is "
                                                          "displayed first")

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.fullname

    def avatar_url(self):
        """
        Returns the URL of the image associated with this Object.
        If an image hasn't been uploaded yet, it returns a stock image
        :returns: str -- the image url
        """
        if self.external_avatar_url:
            return self.external_avatar_url

        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url

        return "{0}{1}/{2}".format(settings.STATIC_URL, 'images',
                                   'user-1633250_640.png')


def default_features():
    return [{"title": "Amazing Community Help", "value": "Yes"},
            {"title": "Access to all materials", "value": "Yes"},
            {"title": "Duration", "value": "5 Days"}]


class Pricing(models.Model):
    name = models.CharField(max_length=100)  # Basic / Pro / Premium
    slug = models.SlugField(max_length=200, unique=True, blank=True, editable=False)
    stripe_price_id = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    currency = models.CharField(max_length=50)
    features = models.JSONField(default=default_features)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Pricing, self.name.lower())

        # Call the "real" save() method.
        super(Pricing, self).save(*args, **kwargs)

    def get_stripe_price(self):
        return int(self.price)  # * 100)

# TODO:
# Add Grant Model
# Add Location/address Model
class Workshop(models.Model):
    codename = models.CharField(max_length=200)
    twitter_hashtags = models.CharField(max_length=200, blank=True,
                                        help_text="Define twitter hashtags. It should start with # and all tags should be separate with a space (no coma or semi-colon")
    slug = models.SlugField(max_length=200, unique=True, blank=True, editable=False)
    start_date = models.DateTimeField(editable=True, default=timezone.now)
    end_date = models.DateTimeField(editable=True, default=timezone.now)
    registration_start_date = models.DateTimeField(editable=True,
                                                   default=timezone.now)
    registration_end_date = models.DateTimeField(editable=True,
                                                 default=timezone.now)
    show_registration_deadline = models.BooleanField(default=False)
    welcome_email = models.TextField(default="Thanks for your joining DIPY Workshop.")
    welcome_email_html = models.TextField(editable=False, blank=True)
    leaflet_image = models.ImageField(upload_to='bg_images/', blank=True,
                                     default=f"{settings.STATIC_URL}/workshop/images/dipy_odf_vs_2018-10-03.png",
                                     help_text="upload leaflet image to the server.")
    speakers = models.ManyToManyField(Speaker, related_name="workshops",
                                      blank=True)
    members = models.ManyToManyField(User, related_name="workshops",
                                     blank=True)
    pricing_tiers = models.ManyToManyField(Pricing, blank=True)
    bg_images = models.ManyToManyField(BackgroundImage,
                                       related_name="workshops",
                                       blank=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    modified = models.DateTimeField(editable=False, auto_now_add=True)
    is_in_person = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    has_live_qa = models.BooleanField(default=True)
    has_live_keynote = models.BooleanField(default=False)
    has_live_demo = models.BooleanField(default=False)
    has_data_accelerator = models.BooleanField(default=True)
    has_code_sprint = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_date']

    @property
    def year(self):
        return self.end_date.year

    @property
    def is_past_due_registration(self):
        return timezone.now() > self.registration_end_date

    def hashtags(self):
        ht = [tag for tag in self.twitter_hashtags.split(' ')
              if '#' in tag or '@' in tag]
        return ht

    def __str__(self):
        return f'DIPY WORKSHOP {self.year}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Workshop, self.__str__().lower())

        html_content = markdown.markdown(self.welcome_email,
                                         extensions=['codehilite'])
        print(html_content)
        # bleach is used to filter html tags like <script> for security
        self.welcome_email_html = bleach.clean(html_content, allowed_html_tags,
                                               allowed_attrs)

        self.modified = timezone.now()
        # clear the cache
        cache.clear()

        # Call the "real" save() method.
        super(Workshop, self).save(*args, **kwargs)


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE,
                                related_name='subscriptions')
    created = models.DateTimeField(auto_now_add=True)
    stripe_session_id = models.CharField(max_length=200, blank=True)
    payment_intent_id = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email

    @property
    def is_active(self):
        return self.status == "active" or self.status == "trialing"


class Track(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="tracks/", blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("workshop:course-detail", kwargs={"slug": self.slug})


class Lesson(Track):
    nb_speakers = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        self.nb_speakers = 0
        if hasattr(self, 'videos'):
            self.nb_speakers = sum([len(v.speakers.all())
                                    for v in self.videos.all()])

        # clear the cache
        cache.clear()

        # Call the "real" save() method.
        super(Lesson, self).save(*args, **kwargs)


class QA(Track):
    panel = models.ManyToManyField(Speaker, related_name="qas",
                                   blank=True)
    zoom_link = models.URLField(max_length=300, blank=True)
    password = models.CharField(max_length=300, blank=True)


class Video(models.Model):
    workshops = models.ManyToManyField(Workshop, related_name="videos",
                                       blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               related_name='videos')
    video_url = models.URLField(max_length=500, blank=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    speakers = models.ManyToManyField(Speaker, related_name="videos",
                                      blank=True)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title

    def video_id(self):
        if not self.video_url:
            return ''

        for prefix in ['https://youtu.be/',
                      'https://www.youtube.com/watch?v=']:
            if self.video_url.startswith(prefix):
                return self.video_url.replace(prefix, '')

        return ''

    def save(self, *args, **kwargs):
        self.lesson.save()

        # clear the cache
        cache.clear()

        # Call the "real" save() method.
        super(Video, self).save(*args, **kwargs)


class WorkshopEvent(models.Model):
    """docstring for WorkshopEvent."""
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE,
                                 related_name='events')
    session = models.ForeignKey(Track, on_delete=models.CASCADE,
                                related_name='events')
    start_date = models.DateTimeField(editable=True, default=timezone.now)
    end_date = models.DateTimeField(editable=True, default=timezone.now)

    def __str__(self):
        return f'Workshop {self.workshop.year} - {self.session.name}'

    class Meta:
        ordering = ["start_date"]
