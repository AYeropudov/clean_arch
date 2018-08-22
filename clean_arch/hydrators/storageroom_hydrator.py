import json


class StorageRoomHydrator(json.JSONEncoder):
    def default(self, o):
        try:
            hydrated = {
                "code": o.code,
                "size": o.size,
                "price": o.price,
                "latitude": o.latitude,
                "longitude": o.longitude
            }
            return hydrated
        except AttributeError:
            return super().default(o)
