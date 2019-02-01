from app.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0ft9*o)sfihe3z3dn$r3g_$*-^xuq5-aq)s#z!4xndx4ia$$pw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}