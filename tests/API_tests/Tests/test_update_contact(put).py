import pytest
import requests
from faker import Faker
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger


@pytest.mark.update_contact_put
def test_update_contact_put(read_config, auth_token, registered_user, logger):
    url_contacts = f"{read_config['URL']}/contacts"

    fake = Faker()
    original_contact = {
        "firstName": fake.first_name_female(),
        "lastName": fake.last_name(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=75).isoformat(),
        "email": fake.unique.email(),
        "phone": fake.msisdn()[:10],
        "street1": fake.street_address(),
        "street2": fake.secondary_address(),
        "city": fake.city(),
        "stateProvince": fake.state_abbr(),
        "postalCode": fake.postcode(),
        "country": fake.country()
    }

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Создание контакта
    response = requests.post(url_contacts, headers=headers, json=original_contact)
    assert response.status_code == 201, f"Ошибка создания контакта: {response.status_code} {response.text}"
    contact_id = response.json().get("_id")
    assert contact_id, "ID контакта не получен"

    updated_contact = original_contact.copy()
    updated_contact["email"] = fake.unique.email()
    updated_contact["phone"] = fake.msisdn()[:10]

    response_put = requests.put(f"{url_contacts}/{contact_id}", headers=headers, json=updated_contact)
    assert response_put.status_code == 200, f"Ошибка обновления PUT: {response_put.status_code} {response_put.text}"

    logger.info(f"Статус: {response.status_code}")
    logger.info("Создан контакт с ID: %s", contact_id)
    logger.info("Контакт обновлён через PUT: ID=%s", contact_id)
    logger.info("Новый email: %s", updated_contact["email"])
    logger.info("Новый телефон: %s", updated_contact["phone"])
