import pytest


@pytest.fixture
def password():
    return "P@ssword!IsVeryLong"


@pytest.fixture
def hashed_password():
    return "$pbkdf2-sha512$25000$GaNUam1NqfUeIwTgPKd0Dg$V6Ls7mbYbrXFFVKt7jjZUqxiZ.uNNv2OjjNvf/tdOKpKFxPSpfH8Jn3zMmeDjamEMr49mZoMC1Fml58MFY7wFA"


@pytest.fixture
def collection():
    return "test_collection"


@pytest.fixture
def data():
    return {
        "_id": "123",
        "name": "test"
    }


@pytest.fixture
def query():
    return {
        "_id": "123"
    }