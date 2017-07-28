from src.common.utils import Utils
from tests.test_common.fixtures import password, hashed_password
from unittest import mock
import pytest

class TestUtils(object):
    def test_check_hashed_password_happy_path(self, password, hashed_password):
        assert Utils.check_hashed_password(password, hashed_password)


    def test_check_hashed_password_wrong_password(self, password, hashed_password):
        assert not Utils.check_hashed_password(password + "1", hashed_password)


    def test_check_hashed_password_wrong_hash(self, password, hashed_password):
        assert not Utils.check_hashed_password(password, hashed_password[:len(hashed_password) - 2] + "AB")


    def test_check_hashed_password_bad_hash(self, password, hashed_password):
        with pytest.raises(ValueError):
            assert not Utils.check_hashed_password(password, hashed_password + "1")


    @mock.patch("passlib.hash.pbkdf2_sha512.encrypt")
    def test_hash_password(self, mock_hash_encrypt, password):
        Utils.hash_password(password)
        assert mock_hash_encrypt.called_with(password)


    EMAIL_IS_VALID_PARAMS = [
        ("test@test.com", True),
        ("t@t.co", True),
        ("tattdotco", False)
    ]
    @pytest.mark.parametrize("email, is_valid_email", EMAIL_IS_VALID_PARAMS)
    def test_email_is_valid(self, email, is_valid_email):
        assert (Utils.email_is_valid(email) is None) == (not is_valid_email)

