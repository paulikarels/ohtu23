from entities.user import User
import re
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        if (not username and password):
            raise UserInputError("Username taken!")
        if (len(username) < 3 ):
            raise UserInputError("Username too short. Minimum of 3 characters.")
        if not (re.match("^[a-z]+$", username) and password):
            raise UserInputError("Invalid username.")
        if (password and len(password) < 8):
            raise UserInputError("Password too short.")
        if (not re.search(r'\d', password) and username):
            raise UserInputError("Password has to be 8 characters and has to contains something else other than letters.")
        if( password != password_confirmation):
            raise UserInputError("Non matching passwords")


user_service = UserService()
