import json

from clean_arch.hydrators.storageroom_hydrator import StorageRoomHydrator
from clean_arch.domain.storageroom import StorageRoom


def test_hydrate_domain_storageroom():
    room = StorageRoom(
        code='643718ea-895d-4f8d-a773-d40115ac659b',
        size=200,
        price=10,
        latitude='-0.000000',
        longitude='1.000000'
    )
    expected_json = """
    {
      "code": "643718ea-895d-4f8d-a773-d40115ac659b",
      "size": 200,
      "price": 10,
      "latitude":"-0.000000",
      "longitude":"1.000000"
    }
    """
    assert json.loads(json.dumps(room, cls=StorageRoomHydrator)) == json.loads(expected_json)

