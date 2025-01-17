from aiocache import cached

from . import db


class Region(db.Model):
    __tablename__ = 'regions'

    region_id = db.Column(db.SmallInteger, primary_key=True)
    region_name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    @classmethod
    @cached(key="Region.all", alias="default")
    async def all(cls):
        result = await Region.query.gino.all()
        return result


@cached(key="Region.dict", alias="default")
async def get_regions_dict():
    result = await db.all(Region.query)
    regions_dict = [
        (i.region_id, (i.region_name, i.latitude, i.longitude))
        for i in result
    ]
    return dict(regions_dict)
