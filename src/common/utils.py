from passlib.hash import pbkdf2_sha512
import re

class Utils(object):
    @staticmethod
    def check_hashed_password(password, pw_hash):
        """
        Hashes the password and compares it against the password hash (pw_hash).
        :param password: Submitted password for user.
        :param pw_hash: Copy of user's password hash stored on the DB.
        :return: True if hashed password matches pw_hash, otherwise False.
        """
        return pbkdf2_sha512.verify(password, pw_hash)


    @staticmethod
    def hash_password(password):
        """
        Hashes supplied password with SHA-512
        :param password: Plaintext password to be hashed.
        :return: SHA-512 hash of plaintext password.
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def email_is_valid(email):
        return re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)").match(email)
