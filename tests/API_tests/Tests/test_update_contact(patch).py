import pytest
import requests
from faker import Faker
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger


@pytest.mark.update_contact_patch
def test_update_contact_patch(read_config, auth_token, registered_user, logger):
    url_contacts = f"{read_config['URL']}/contacts"

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

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

    r_post = requests.post(url_contacts, headers=headers, json=contact_payload)
    assert r_post.status_code == 201, f"Ошибка при создании контакта: {r_post.status_code} {r_post.text}"
    contact_id = r_post.json().get("_id")

    # Шаг 2: обновляем контакт через PATCH
    patch_payload = {
        "email": fake.unique.email(),
        "phone": fake.msisdn()[:10]
    }

    r_patch = requests.patch(f"{url_contacts}/{contact_id}", headers=headers, json=patch_payload)
    assert r_patch.status_code == 200, f"Ошибка PATCH-запроса: {r_patch.status_code} {r_patch.text}"

    # Проверки
    updated = r_patch.json()
    assert updated["email"] == patch_payload["email"]
    assert updated["phone"] == patch_payload["phone"]

    logger.info(f"Статус: {r_patch.status_code}")
    logger.info("Создан контакт с ID: %s", contact_id)
    logger.info("Обновлённые данные: email=%s, phone=%s", updated['email'], updated['phone'])
    logger.info("PATCH прошёл успешно для пользователя %s %s", registered_user['firstName'],
                registered_user['lastName'])
