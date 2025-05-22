import pytest
import requests
from faker import Faker
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger, headers


@pytest.mark.add_contact
def test_add_contact(read_config, auth_token, registered_user, logger, headers):
    url = f"{read_config['URL']}/contacts"

    fake = Faker()

    contact_payload = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat(),
        "email": fake.unique.email(),
        "phone": fake.msisdn()[:10],
        "street1": fake.street_address(),
        "street2": fake.secondary_address(),
        "city": fake.city(),
        "stateProvince": fake.state_abbr(),
        "postalCode": fake.postcode(),
        "country": fake.country()
    }

    response = requests.post(url, headers=headers, json=contact_payload)

    response_json = response.json()

    # Checks
    assert response.status_code == 201, f"Contact not created: {response.status_code}, {response.text}"
    assert response_json["firstName"] == contact_payload["firstName"]
    assert response_json["email"] == contact_payload["email"]
    assert "_id" in response_json

    logger.info(f"Status: {response.status_code}")
    logger.info(f"Response: {response.text}")
