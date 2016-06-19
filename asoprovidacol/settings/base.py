# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z!tgkgn=93vcdhu9^eb_#i6vev8_!x9s@@y0&d+vum_ir7mk-p'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.middleware.locale.LocaleMiddleware',

)

THIRD_PARTY_APPS = (
)

LOCAL_APPS = (

    'home',
    'agenda.apps.AgendaConfig',
    'topics.apps.TopicsConfig',
    'projects.apps.ProjectsConfig',
    'rooms.apps.RoomsConfig',
    'profiles.apps.ProfilesConfig',
    'pages.apps.PagesConfig',
    'country.apps.CountryConfig',
    'activities.apps.ActivitiesConfig',


)

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('login')
LOGOUT = reverse_lazy('logout')

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'asoprovidacol.urls'

WSGI_APPLICATION = 'asoprovidacol.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-CO'
TIME_ZONE = 'America/Bogota'
#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]
#AUTH_USER_MODEL = 'users.User'
