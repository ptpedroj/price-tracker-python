from src.models.users.constants import UserConstants
from src.models.users.user import User
import src.models.users.errors as errors
from tests.test_models.test_users.fixtures import user, email, password, hashed_password, user_id
import pytest
import unittest.mock as mock


class TestUser(object):
    def test_create_user(self, email, password, user_id):
        test_user = User(email, password, user_id)
        assert test_user.email == email and \
            test_user.password == password and \
            test_user._id == user_id


    def test_user_repr(self, user):
        assert repr(user) == repr(eval(repr(user)))


    def test_user_str(self, user, email, user_id):
        assert str(user).startswith("<User")


    @mock.patch("src.common.database.Database.find_one")
    def test_is_login_valid_happy_path(self, mock_db_find_one, hashed_password, email, password):
        mock_db_find_one.return_value = {"password": hashed_password}
        assert User.is_login_valid(email, password)


    @mock.patch("src.common.database.Database.find_one")
    def test_is_login_valid_bad_email(self, mock_db_find_one, hashed_password, email, password):
        mock_db_find_one.return_value = None
        with pytest.raises(errors.UserNotExistsError):
            assert User.is_login_valid(email, password)


    @mock.patch("src.common.database.Database.find_one")
    def test_is_login_valid_bad_password(self, mock_db_find_one, hashed_password, email, password):
        mock_db_find_one.return_value = {"password": hashed_password}
        with pytest.raises(errors.IncorrectPasswordError):
            assert User.is_login_valid(email, password + "1")


    @mock.patch("src.common.database.Database.find_one")
    @mock.patch("src.models.users.user.User.save_to_db")
    def test_register_user_happy_path(self, mock_user_save_to_db, mock_db_find_one, email, password):
        mock_db_find_one.return_value = None
        is_user_created = User.register_user(email, password)
        assert is_user_created and mock_user_save_to_db.called


    @mock.patch("src.common.database.Database.find_one")
    @mock.patch("src.models.users.user.User.save_to_db")
    def test_register_user_bad_email(self, mock_user_save_to_db, mock_db_find_one, email, password):
        mock_db_find_one.return_value = None
        with pytest.raises(errors.InvalidEmailError):
            User.register_user(email[:3], password)


    @mock.patch("src.common.database.Database.find_one")
    @mock.patch("src.models.users.user.User.save_to_db")
    def test_register_user_already_registered(self, mock_user_save_to_db, mock_db_find_one, email, password):
        mock_db_find_one.return_value = user.__dict__
        with pytest.raises(errors.UserAlreadyRegisteredError):
            User.register_user(email, password)


    @mock.patch("src.common.database.Database.insert")
    def test_save_to_db(self, mock_db_insert, user):
        user.save_to_db()
        assert mock_db_insert.called_with(UserConstants.COLLECTION, user.json())


    def test_json(self, user):
        user_json = user.json()
        assert user_json["_id"] == user._id and \
            user_json["email"] == user.email and \
            user_json["password"] == user.password


    @mock.patch("src.common.database.Database.find_one")
    def test_get_by_id(self, mock_db_find_one, user, user_id):
        mock_db_find_one.return_value = user.__dict__
        test_user = User.get_by_id(user_id)
        assert repr(test_user) == repr(user) and \
            mock_db_find_one.called_with(UserConstants.COLLECTION, {"_id": user_id})