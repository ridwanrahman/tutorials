import re, contextlib
from contextvars import ContextVar, Token
from dataclasses import dataclass
from typing import Generator

validation_context: ContextVar[bool] = ContextVar("validation_context", default=True)

@contextlib.contextmanager
def using_validation_context(validate: bool) -> Generator[None, None, None]:
    token: Token[bool] = validation_context.set(validate)

    try:
        yield
    finally:
        validation_context.reset(token)

class UserName(str):
    USERNAME_PATTERN = re.compile(r"[a-zA-Z0-9_-]+$")

    def __new__(cls, value: str) -> "UserName":
        validate = validation_context.get()
        if validate:
            if not value:
                raise ValueError("Username cannot be empty")
            if len(value) > 20:
                raise ValueError("Username is too long")
            if len(value) < 3:
                raise ValueError("Username is too short")

            if not cls.USERNAME_PATTERN.fullmatch(value):
                raise ValueError("Username is not valid")

        return super().__new__(cls, value)

class Email(str):
    EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    def __new__(cls, value: str) -> "Email":
        validate = validation_context.get()
        if validate:
            if not value:
                raise ValueError("Email cannot be empty")

            if not cls.EMAIL_PATTERN.fullmatch(value):
                raise ValueError("Invalid email")

        return super().__new__(cls, value)

@dataclass
class User:
    username: UserName
    email: Email