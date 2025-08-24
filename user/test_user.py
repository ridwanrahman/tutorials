import pytest
from user.User import UserName, Email

def test_valid_username() -> None:
    username = UserName("john")
    assert username == "john"

def test_invalid_username() -> None:
    with pytest.raises(ValueError) as excinfo:
        username = UserName("&&&&as")
    assert "Username is not valid" in str(excinfo)


def test_valid_email() -> None:
    email = Email("ridwan@test.com")
    assert email == "ridwan@test.com"

