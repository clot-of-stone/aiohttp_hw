import json

from aiohttp import web
from sqlalchemy.exc import IntegrityError

from models import ORM_MODEL, ORM_MODEL_CLS


async def get_obj(object_id: int, model_class: ORM_MODEL_CLS, session):
    found_object = await session.get(model_class, object_id)
    if found_object is None:
        raise web.HTTPNotFound(
            text=json.dumps(
                {'status': 'error', 'message': 'object not found'}),
            content_type='application/json'
        )
    return found_object


async def create_obj(model_class: ORM_MODEL_CLS, session, **params):
    new_object = model_class(**params)
    session.add(new_object)
    try:
        await session.commit()
    except IntegrityError as error:
        raise web.HTTPConflict(
            text=json.dumps({'error': 'user already exists'}),
            content_type='application/json'
        )
    return new_object


async def patch_obj(object: ORM_MODEL, session, **params):
    for field, value in params.items():
        setattr(object, field, value)
    session.add(object)
    await session.commit()


async def delete_obj(object: ORM_MODEL, session):
    await session.delete(object)
    await session.commit()
