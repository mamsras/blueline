"""
ASGI config for dashboard project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
from api.routing import websocket_urlpatterns
from api.middlewares import TokenAuthMiddleWare  # Assurez-vous que le chemin vers TokenAuthMiddleWare est correct

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleWare(  # Utilisation du middleware d'authentification personnalisé
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
