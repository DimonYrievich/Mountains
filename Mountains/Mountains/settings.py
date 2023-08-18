
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ly)0%e8fq=q=lfibp1vrdc49r#mdr#c!386g!b#y15g$%@72p8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Point',
    'rest_framework',                                # Добавляем django_rest_framework в список установленных приложений
    'django.contrib.sites',                                    # Подключаем приложение для работы с плоскими страничками
	'django.contrib.flatpages',                                # Подключаем приложение для работы с плоскими страничками
    'django_filters',                                                    # Чтобы получить доступ к фильтрам в приложении
    'sign',                                                       # Приложение регистрации, аутентификации и авторизации
    'protect',                        # Для обеспечения безопасности и защиты приложения от несанкционированного доступа
    ]

SITE_ID = 1                                               # добавим переменную SITE_ID для работы с плоскими страничками

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     #добавим, чтобы наше новое приложение отработало корректно
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
    ]

ROOT_URLCONF = 'Mountains.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],     # Полностью заменяем строку на эту. Такая настройка указывает
        'APP_DIRS': True,                                            #Django искать шаблоны в соответствующей директории
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Mountains.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# AUTH_USER_MODEL = 'Point.Users'             # Указываем модель для аутентификации пользователя, если есть обязательные
                                                                                                   # поля для заполнения

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATICFILES_DIRS = [                                                               # Чтобы проект знал, где искать стили
    BASE_DIR / "static"
]


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Настройка медиа-папки
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_URL = 'sign/login/'                   # Для конкретизации URL-адреса, на котором находится страница аутентификации
LOGIN_REDIRECT_URL = '/'                      # Страница, на которую перенаправляется пользователь после успешного входа
                                                                      # на сайт, в данном случае корневая страница сайта


########################################################################################################################