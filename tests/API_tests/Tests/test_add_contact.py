import pytest
import requests
from faker import Faker
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger


@pytest.mark.add_contact
def test_add_contact(read_config, auth_token, registered_user, logger):
    url = f"{read_config['URL']}/contacts"

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

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

    # Проверки
    assert response.status_code == 201, f"Контакт не создан: {response.status_code}, {response.text}"
    assert response_json["firstName"] == contact_payload["firstName"]
    assert response_json["email"] == contact_payload["email"]
    assert "_id" in response_json

    logger.info(f"Статус: {response.status_code}")
    logger.info(f"Ответ: {response.text}")
