# Django settings for myproject project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
GRAPPELLI_ADMIN_TITLE = "HM Admin"
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'data.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/Users/huymac/Testingcode/myproject/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/Users/huymac/Testingcode/myproject/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://127.0.0.1:8000/static/'
ADMIN_MEDIA_PREFIX = '/Users/huymac/Testingcode/myproject/media/admin/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'af33ej!*ng0%--o-jw07kkpmtgela))@zh0u(4gn#^377$ya$s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
                              'django.contrib.auth.context_processors.auth',
'django.core.context_processors.debug',
'django.core.context_processors.i18n',
'django.core.context_processors.media',
'django.core.context_processors.static',
'django.contrib.messages.context_processors.messages',
 'django.core.context_processors.request',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'contentmanager.middleware.EditmodeMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'myproject.wsgi.application'

TEMPLATE_DIRS = (
                 "/Users/huymac/Testingcode/myproject/templates"
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


INSTALLED_APPS = (                    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.comments',
    'django.contrib.staticfiles',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'taggit',
    'taggit_templatetags',
    'quix.django.contact',
    'captcha',
    'cartridge',
    'tastypie',
    'todo',
    'django.contrib.sitemaps',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'blog',
    'shop',
    'book',
    'page',
    'tastypie',
    'backbone_tastypie',
)
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
RECAPTCHA_PUBLIC_KEY = '6LcgydcSAAAAAJjfGJpP3RXdA7x6zYPdAvnf30Ge'
RECAPTCHA_PRIVATE_KEY = '6LcgydcSAAAAAIH4p7CF4PzXpHOsD-WaHXLFZiP_'
CONTACT_EMAILS = ('macanhhuydn@gmail.com',)
CONTACT_FORM_CLASS = 'myproject.forms.ReCaptchaContactForm'

#TINYMCE_DEFAULT_CONFIG = {
#'theme': "advanced",
#'theme_advanced_toolbar_location' : "top",
# 'plugins': 'table,advimage,advlink,inlinepopups,preview,media,searchreplace,contextmenu,paste,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template',
#    'theme_advanced_buttons1': 'fullscreen,|,bold,italic,underline,strikethrough,|,sub,sup,|,bullist,numlist,|,outdent,indent,|,formatselect,removeformat',
#    'theme_advanced_buttons2': 'cut,copy,paste,pastetext,pasteword,|,search,replace,|,undo,redo,|,link,unlink,anchor,image,media,charmap,|,visualchars,nonbreaking',
#    'theme_advanced_buttons3': 'visualaid,tablecontrols,|,blockquote,del,ins,|,preview,code,template',
# 'relative_urls': False,
#    'width': 600,
#    'height': 300,    
#}
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
