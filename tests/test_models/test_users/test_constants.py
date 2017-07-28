from src.models.users.constants import UserConstants

class TestConstants(object):
    def test_has_collection_constant(self):
        assert hasattr(UserConstants, "COLLECTION")
