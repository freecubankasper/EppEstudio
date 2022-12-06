import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=str(os.path.join(str(BASE_DIR), '.env')))

"""   
    PRODUCTION = 1 -->  Cargar las variables desde las variables entorno del sistema
    PRODUCTION = 0 -->  Cargar las variables desde el archivo .env

"""

PRODUCTION = bool(int(os.environ.get('PRODUCTION', os.getenv('PRODUCTION'))))
if PRODUCTION:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = bool(int(os.environ.get('DEBUG')))
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DB_ENGINE'),
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }

else:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # DEBUG = not PRODUCTION
    DEBUG = True
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE'),
            'NAME': os.getenv('POSTGRES_NAME'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT'),
        }
    }