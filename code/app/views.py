from aiohttp import web
from bcrypt import hashpw, gensalt

from crud import get_obj, create_obj, patch_obj, delete_obj
from models import Advertisement, User


class AdvView(web.View):

    async def get(self):
        adv = await get_obj(int(self.request.match_info['advertisement_id']),
                            Advertisement, self.request['session'])
        return web.json_response({
            'id': adv.id,
            'owner': adv.owner_id,
            'title': adv.title,
            'description': adv.description,
            'created at': int(adv.creation_time.timestamp())
        })

    async def post(self):
        json_data = await self.request.json()
        new_adv = await create_obj(Advertisement, self.request['session'],
                                   **json_data)
        return web.json_response({'id': new_adv.id})

    async def patch(self):
        adv = await get_obj(int(self.request.match_info['advertisement_id']),
                            Advertisement, self.request['session'])
        json_data = await self.request.json()
        await patch_obj(adv, self.request['session'], **json_data)
        return web.json_response({'status': 'update succeeded'})

    async def delete(self):
        adv = await get_obj(int(self.request.match_info['advertisement_id']),
                            Advertisement, self.request['session'])
        await delete_obj(adv, self.request['session'])
        return web.json_response({'status': 'delete succeeded'})


class UserView(web.View):

    async def get(self):
        user = await get_obj(int(self.request.match_info['user_id']), User,
                             self.request['session'])
        return web.json_response({
            'id': user.id,
            'email': user.email
        })

    async def post(self):
        json_data = await self.request.json()
        json_data['password'] = hashpw(json_data['password'].encode(),
                                       salt=gensalt()).decode()
        new_user = await create_obj(User, self.request['session'], **json_data)

        return web.json_response({'id': new_user.id})

    async def patch(self):
        user = await get_obj(int(self.request.match_info['user_id']), User,
                             self.request['session'])
        json_data = await self.request.json()
        await patch_obj(user, self.request['session'], **json_data)
        return web.json_response({'status': 'update succeeded'})

    async def delete(self):
        user = await get_obj(int(self.request.match_info['user_id']), User,
                             self.request['session'])
        await delete_obj(user, self.request['session'])
        return web.json_response({'status': 'delete succeeded'})
