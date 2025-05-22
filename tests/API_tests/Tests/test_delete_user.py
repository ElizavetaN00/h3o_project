import pytest
import requests
from tests.API_tests.conftest import read_config, registered_user, logger


@pytest.mark.delete_user
def test_delete_user(read_config, registered_user, logger):
    base_url = read_config['URL']

    login_payload = {
        "email": registered_user["email"],
        "password": registered_user["password"]
    }

    r_login = requests.post(f"{base_url}/users/login", json=login_payload)
    assert r_login.status_code == 200, f"Authorization failed: {r_login.status_code} {r_login.text}"
    token = r_login.json().get("token")
    assert token, "Token not received"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    r_delete = requests.delete(f"{base_url}/users/me", headers=headers)

    # Checks
    assert r_delete.status_code == 200, f"Removal failed: {r_delete.status_code} {r_delete.text}"
    assert r_delete.text.strip() == "", "The answer when deleting must be empty"

    logger.info("User successfully deleted.")
    logger.info(f"Status: {r_delete.status_code}")
