from clean_arch.use_cases import  request_objects as ro


def test_build_storage_room_list_ro_without_params():
    request = ro.StorageRoomListRequestObject()
    assert bool(request) is True

def test_build_storage_room_list_ro():
    request = ro.StorageRoomListRequestObject.from_dict({})
    assert bool(request) is True
