import pytest
from tests.API_tests.conftest import registered_user, logger

@pytest.mark.add_user
def test_add_user(registered_user, logger):

    # Checking that all required fields are returned
    assert "email" in registered_user
    assert "password" in registered_user
    assert "firstName" in registered_user
    assert "lastName" in registered_user

    # Checks
    assert len(registered_user["password"]) >= 8

    logger.info(f"User successfully created: {registered_user['email']},{registered_user['password']}")
