from tests.test_models.test_users.fixtures import message
import pytest
import src.models.users.errors as errors


EXCS = [
    errors.UserError,
    errors.UserNotExistsError,
    errors.IncorrectPasswordError,
    errors.UserAlreadyRegisteredError,
    errors.InvalidEmailError
]


class TestErrors(object):
    def test_exists_usererror(self):
        assert issubclass(errors.UserError, Exception)


    def test_exists_usernotexistserror(self):
        assert issubclass(errors.UserNotExistsError, errors.UserError)


    def test_exists_incorrectpassworderror(self):
        assert issubclass(errors.IncorrectPasswordError, errors.UserError)


    def test_exists_useralreadyregisterederror(self):
        assert issubclass(errors.UserAlreadyRegisteredError, errors.UserError)


    def test_exists_invalidemailerror(self):
        assert issubclass(errors.InvalidEmailError, errors.UserError)


    @pytest.mark.parametrize('exc', EXCS)
    def test_error_holds_message(self, exc, message):
        error = exc(message)
        assert error.message == message