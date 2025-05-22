import pytest
import requests
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger, headers


@pytest.mark.get_user_profile
def test_get_user_profile(read_config, auth_token, registered_user, logger, headers):
    url = f"{read_config['URL']}/users/me"

    response = requests.get(url, headers=headers)

    data = response.json()

    # Checks
    assert response.status_code == 200, f"Expected code 200, but received {response.status_code}"
    assert "firstName" in data, "The firstName field is missing"
    assert "email" in data, "Email field is missing"

    logger.info(f"Status: {response.status_code}")
    logger.info(f"User data received: {data}")
