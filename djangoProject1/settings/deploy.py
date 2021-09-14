from .base import *

env_list = dict()

local_env = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_env.readline()
    if not line:
        break
    # 줄바꿈 문자를 공백으로 바꿔줌
    line = line.replace('\n', '')

    # '='의 위치를 찾아줌. =을 기준으로 왼쪽이 key, 오른쪽이 value
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]

    env_list[key] = value


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}