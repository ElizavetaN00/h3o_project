import pytest
import requests
from faker import Faker
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger


@pytest.mark.delete_contact
def test_create_and_delete_contact(read_config, auth_token, registered_user, logger):
    url_contacts = f"{read_config['URL']}/contacts"

    fake = Faker()
    contact_payload = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
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
    r_create = requests.post(url_contacts, headers=headers, json=contact_payload)
    assert r_create.status_code == 201, f"Контакт не создан: {r_create.status_code} {r_create.text}"
    contact_id = r_create.json().get("_id")
    assert contact_id, "ID контакта не получен из ответа"

    # Удаление созданного контакта
    r_delete = requests.delete(f"{url_contacts}/{contact_id}", headers=headers)
    logger.info(f"Удаление контакта:{r_delete.status_code}, {r_delete.text}")
    assert r_delete.status_code == 200, "Контакт не был удалён"

    # Проверка, что контакт удалён
    r_check = requests.get(f"{url_contacts}/{contact_id}", headers=headers)
    assert r_check.status_code in [404, 400], "Контакт всё ещё существует после удаления"

    logger.info(f"Контакт успешно удалён и больше не существует: {contact_id}")
    logger.info(f"Cтатус: {r_check.status_code}")
