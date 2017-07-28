import src.models.users.errors as UserErrors
import uuid
from src.common.database import Database
from src.common.utils import Utils
from src.models.users.constants import UserConstants

class User(object):
    def __init__(self, email, password, _id = None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id


    def __repr__(self):
        return f"User('{self.email}', '{self.password}', '{self._id}')"


    def __str__(self):
        return f"<User {self.email} with ID {self._id}>"


    @staticmethod
    def is_login_valid(email, password):
        """
        Verifies that an email / password combo (as submitted through the site forms) is valid.
        Checks that the email exists and the password is correct.
        
        :param email: User's email.
        :param password: SHA512 hashed password
        :return: true if email exists and password hashes match, otherwise false.
        """
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            # Tell user data does not exist.
            raise UserErrors.UserNotExistsError(f"User {email} does not exist or password is incorrect.")

        elif not Utils.check_hashed_password(password, user_data["password"]):
            # Tell user either their password or email address is wrong.
            raise UserErrors.IncorrectPasswordError(f"User {email} does not exist or password is incorrect.")

        else:
            return True

    @staticmethod
    def register_user(email, password):
        """
        Register a user with the DB
        :param email: User's email.
        :param password: User's password.
        :return: True if registered successfully or exceptions otherwise.
        """
        user_data = Database.find_one("users", {"email": email})

        if user_data is None:
            if Utils.email_is_valid(email):
                User(email, Utils.hash_password(password)).save_to_db()
                return True
            else:
                raise UserErrors.InvalidEmailError(f"{email} is not a valid email address.")
        else:
            raise UserErrors.UserAlreadyRegisteredError(f"{email} is already registered.")



    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }


    def save_to_db(self):
        Database.insert(UserConstants.COLLECTION, self.json())


    @classmethod
    def get_by_id(cls, _id):
        return cls(**Database.find_one(UserConstants.COLLECTION, {"_id": _id}))