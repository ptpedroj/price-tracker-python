from src.common.utils import Utils
from src.models.users.user import User
import pytest


@pytest.fixture
def email():
    return "test_user@test.com"


@pytest.fixture
def message():
    return "test message"


@pytest.fixture
def password():
    return "password"


@pytest.fixture
def hashed_password(password):
    return Utils.hash_password(password)


@pytest.fixture
def user_id():
    return "1234"


@pytest.fixture
def user(email, password, user_id):
    return User(email, password, user_id)