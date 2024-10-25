import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from emails import routing as emails_routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_integration.settings")
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(emails_routing.websocket_urlpatterns)
        )
    ),
})
