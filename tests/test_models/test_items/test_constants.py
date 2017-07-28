from src.models.items.constants import ItemConstants

class TestConstants(object):
    def test_has_collection_constant(self):
        assert hasattr(ItemConstants, "COLLECTION")
