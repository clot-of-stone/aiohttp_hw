from aiohttp import web

from app_db import Session


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with Session() as session:
        request['session'] = session
        res = await handler(request)
        return res
