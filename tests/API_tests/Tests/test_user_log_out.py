import pytest
import requests
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger, headers


@pytest.mark.logout
def test_user_logout(read_config, auth_token, registered_user, logger, headers):
    url = f"{read_config['URL']}/users/logout"

    response = requests.post(url, headers=headers)

    # Checks
    assert response.status_code == 200
    assert response.text.strip() == ""  # the response body must be empty

    logger.info(f"Status: {response.status_code}")
    logger.info(f"Response: '{response.text}'")

