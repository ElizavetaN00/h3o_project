import pytest
import requests
from faker import Faker
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger



@pytest.mark.get_contact_list
def test_get_contact_list(read_config, auth_token, registered_user, logger):
    url = f"{read_config['URL']}/contacts"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    fake = Faker()
    def generate_contact():
        return {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            "email": fake.unique.email(),
            "phone": fake.msisdn()[:10],
            "street1": fake.street_address(),
            "street2": fake.secondary_address(),
            "city": fake.city(),
            "stateProvince": fake.state_abbr(),
            "postalCode": fake.postcode(),
            "country": fake.country()
        }

    # Создание первого контакта
    contact_1 = generate_contact()
    response_1 = requests.post(url, headers=headers, json=contact_1)
    assert response_1.status_code == 201, f"Ошибка при создании 1 контакта: {response_1.status_code} {response_1.text}"

    # Создание второго контакта
    contact_2 = generate_contact()
    response_2 = requests.post(url, headers=headers, json=contact_2)
    assert response_2.status_code == 201, f"Ошибка при создании 2 контакта: {response_2.status_code} {response_2.text}"

    # Получение списка контактов
    r_get = requests.get(url, headers=headers)
    assert r_get.status_code == 200, "Не удалось получить список контактов"
    contacts = r_get.json()
    assert len(contacts) >= 2, "В списке должно быть как минимум два контакта"

    logger.info(f"Контакт-лист успешно получен: {r_get.text}")
    logger.info(f"Статус: {r_get.status_code}")
