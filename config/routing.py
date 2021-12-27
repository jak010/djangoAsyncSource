from channels.auth import SessionMiddleware,CookieMiddleware

from channels.routing import ProtocolTypeRouter, URLRouter
import appws.routing

application = ProtocolTypeRouter({

    'websocket': CookieMiddleware(
        URLRouter(
            appws.routing.websocket_urlpatterns
        )
    )

})
