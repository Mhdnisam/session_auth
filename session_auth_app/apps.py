from django.apps import AppConfig


class SessionAuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'session_auth_app'

    def ready(self):

        import session_auth_app.signals