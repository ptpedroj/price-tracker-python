from src.models.stores.constants import StoreConstants

class TestConstants(object):
    def test_has_collection_constant(self):
        assert hasattr(StoreConstants, "COLLECTION")
