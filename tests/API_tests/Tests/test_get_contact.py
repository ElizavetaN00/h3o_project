import pytest
import requests
from tests.API_tests.conftest import read_config, auth_token, created_contact_id, registered_user, logger, headers


@pytest.mark.get_contact
def test_get_contact(read_config, auth_token, created_contact_id, registered_user, logger, headers):
    url = f"{read_config['URL']}/contacts/{created_contact_id}"

    response = requests.get(url, headers=headers)

    contact = response.json()

    # Checks
    assert response.status_code == 200, "Failed to get contact"
    assert contact["_id"] == created_contact_id, "Contact ID does not match"
    assert "firstName" in contact and "email" in contact, "Incorrect response structure"

    logger.info(f"Contact received: {response.text}")
    logger.info(f"Status: {response.status_code}")
