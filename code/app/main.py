from aiohttp import web

from context import app_context
from middleware import session_middleware
from views import AdvView, UserView

app_site = web.Application()

app_site.cleanup_ctx.append(app_context)
app_site.middlewares.append(session_middleware)

app_site.add_routes([
    web.get('/ads/{advertisement_id:\d+}', AdvView),
    web.post('/ads', AdvView),
    web.patch('/ads/{advertisement_id:\d+}', AdvView),
    web.delete('/ads/{advertisement_id:\d+}', AdvView),
    web.get('/users/{user_id:\d+}', UserView),
    web.post('/users', UserView),
    web.patch('/users/{user_id:\d+}', UserView),
    web.delete('/users/{user_id:\d+}', UserView)
])

if __name__ == '__main__':
    web.run_app(app_site)
