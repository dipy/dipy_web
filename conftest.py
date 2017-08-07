import os
import pytest
import django
from django.conf import settings
# We manually designate which settings we will be using in an environment variable
# This is similar to what occurs in the `manage.py`
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dipy_web.test_settings')

# `pytest` automatically calls this function once when tests are run.
def pytest_configure():
    settings.DEBUG = False
    # settings.configure(
    #     DEBUG_PROPAGATE_EXCEPTIONS=True,
    #     DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
    #                            'NAME': ':memory:'}},
    #     SITE_ID=1,
    #     SECRET_KEY='not very secret in tests',
    #     USE_I18N=True,
    #     USE_L10N=True,
    #     INSTALLED_APPS=(
    #         'django.contrib.auth',
    #         'django.contrib.contenttypes',
    #         'django.contrib.sessions',
    #         'django.contrib.sites',
    #         'django.contrib.messages',
    #         'django.contrib.staticfiles',
    #         'tests',
    #     ),
    #     ROOT_URLCONF='tests.urls',
    #     MIDDLEWARE_CLASSES=(
    #         'django.contrib.sessions.middleware.SessionMiddleware',
    #         'django.contrib.messages.middleware.MessageMiddleware',
    #     ),
    #     TEMPLATES=[
    #         {
    #             'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #             'OPTIONS': {
    #                 'context_processors': [
    #                     'django.template.context_processors.debug',
    #                     'django.template.context_processors.request',
    #                     'django.contrib.auth.context_processors.auth',
    #                     'django.contrib.messages.context_processors.messages',
    #                 ],
    #                 'loaders': [
    #                     'django.template.loaders.filesystem.Loader',
    #                     'django.template.loaders.app_directories.Loader'
    #                 ],
    #             },
    #         },
    #     ]
    # )
    # If you have any test specific settings, you can declare them here,
    # e.g.
    # settings.PASSWORD_HASHERS = (
    #     'django.contrib.auth.hashers.MD5PasswordHasher',
    # )
    django.setup()
    # Note: In Django =< 1.6 you'll need to run this instead
    # settings.configure()

@pytest.fixture
def random_user(scope="module"):
    from django.contrib.auth.models import User
    user = User(username='J-D',
                first_name='John',
                last_name='Doe',
                email='jd@gmail.com',
                )
    user.set_password('pwd_test2!')
    return user

@pytest.fixture
def random_admin_user(scope="module"):
    user = random_user()
    user.is_superuser = True
    return user
