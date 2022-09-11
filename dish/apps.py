from django.apps import AppConfig

DISH_APP_LABEL = 'dish'


class SharedServiceLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = f'{DISH_APP_LABEL}'
