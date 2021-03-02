"""More info in
https://www.caktusgroup.com/blog/2019/04/26/how-switch-custom-django-user-model-mid-project
https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html

"""

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MyUserManager(BaseUserManager):

    def create_user(self, username, email=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user_via_email(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address or a username + token')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser_via_email(self, email=None, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255,
                              unique=True)
    avatar = models.ImageField(upload_to='avatar_images/', blank=True,
                               null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()


    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.email

    @property
    def have_gh_permission(self):
        return self.is_admin

    def avatar_url(self):
        """
        Returns the URL of the image associated with this Object.
        If an image hasn't been uploaded yet, it returns a stock image
        :returns: str -- the image url
        """
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "{0}{1}/{2}".format(settings.STATIC_URL, 'images', 'user-1633250_640.png')