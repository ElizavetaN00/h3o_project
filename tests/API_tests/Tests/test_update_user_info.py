import pytest
import requests
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger, headers


@pytest.mark.update_user_info
def test_update_user_info(read_config, auth_token, registered_user, logger, headers):
    url = f"{read_config['URL']}/users/me"

    new_password = "UpdatedPass456!"
    updated_payload = {
        "firstName": "Updated",
        "lastName": "User",
        "email": registered_user["email"],
        "password": new_password
    }

    response = requests.patch(url, headers=headers, json=updated_payload)

    json_data = response.json()

    # Checks
    assert response.status_code == 200
    assert json_data["firstName"] == "Updated"
    assert json_data["lastName"] == "User"

    logger.info(f"User info updated: status {response.status_code}, response: {response.text}")
