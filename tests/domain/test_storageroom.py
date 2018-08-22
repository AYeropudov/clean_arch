import uuid
from clean_arch.domain.storageroom import StorageRoom


def test_storageroom_model_init():
    code = uuid.uuid4()
    storage_room = StorageRoom(
        code=code,
        size=200,
        price=10,
        latitude='-0.000000',
        longitude='0.888888'
    )
    assert storage_room.code == code
    assert storage_room.size == 200
    assert storage_room.price == 10
    assert storage_room.latitude == '-0.000000'
    assert storage_room.longitude == '0.888888'


def test_storageroom_model_from_dict():
    code = uuid.uuid4()
    storage_room = StorageRoom.from_dict({
        'code': code,
        'size': 200,
        'price': 10,
        'latitude': '-0.000000',
        'longitude': '0.888888'
    })
    assert storage_room.code == code
    assert storage_room.size == 200
    assert storage_room.price == 10
    assert storage_room.latitude == '-0.000000'
    assert storage_room.longitude == '0.888888'
