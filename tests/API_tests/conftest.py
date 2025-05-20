import os
import json
import pytest
import requests
import random
import string
from faker import Faker
import logging

fake = Faker()


@pytest.fixture(scope="function")
def read_config():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "API_tests", "Test_Data", "config.json")
    with open(config_path, encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="function")
def registered_user():
    url = "https://thinking-tester-contact-list.herokuapp.com/users"

    email = fake.unique.email()
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

    user_data = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": email,
        "password": password
    }

    response = requests.post(url, json=user_data)
    assert response.status_code == 201, f"Ошибка регистрации: {response.status_code} {response.text}"
    return user_data


@pytest.fixture(scope="function")
def auth_token(registered_user):
    login_url = "https://thinking-tester-contact-list.herokuapp.com/users/login"
    payload = {
        "email": registered_user["email"],
        "password": registered_user["password"]
    }

    response = requests.post(login_url, json=payload)
    assert response.status_code == 200, f"Ошибка авторизации: {response.status_code} {response.text}"
    return response.json()["token"]


@pytest.fixture
def created_contact_id(read_config, auth_token):
    url = f"{read_config['URL']}/contacts"
    contact_payload = {
        "firstName": "Test",
        "lastName": "Contact",
        "birthdate": "1990-01-01",
        "email": fake.unique.email(),
        "phone": "1234567890",
        "street1": "123 Test Street",
        "street2": "",
        "city": "Testville",
        "stateProvince": "TS",
        "postalCode": "00000",
        "country": "Testland"
    }

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=contact_payload)
    assert response.status_code == 201, f"Не удалось создать контакт: {response.status_code} {response.text}"

    contact_id = response.json()["_id"]
    return contact_id


@pytest.fixture
def logger():
    logger = logging.getLogger("test_logger")
    if not logger.handlers:  # Чтобы не добавлялось дважды
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
