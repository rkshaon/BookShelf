# Database Settings
DATABASES_SETTINGS = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_username',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS_SETTINGS = []

SECRET_KEY_SETTINGS = 'projectssecretekey'
CORS_ALLOWED_ORIGINS_SETTINGS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

X_FRAME_OPTIONS_SETTINGS = 'ALLOW-FROM http://localhost:8080'

ELASTICSEARCH_DSL_SETTINGS = {
    'default': {
        'hosts': 'https://elastic:UCPixWsUH8WG_cTtad+F@localhost:9200',
        'http_auth': ('elastic', 'UCPixWsUH8WG_cTtad+F'),
        'verify_certs': False
    },
}

FRONTEND_BASE_URL_SETTINGS = ''
