import pytest
import requests
import json
import os
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.update_contact_put
def test_update_contact(read_config):
    url_contacts = f"{read_config['URL']}/contacts"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.normpath(os.path.join(current_dir, '..', 'Test_Data'))
    contact_ids_file = os.path.join(test_data_dir, 'contact_ids.json')
    second_template_file = os.path.join(test_data_dir, 'second_contact_template.json')

    token = load_token()

    # Данные второго контакта
    second_contact_payload = {
        "firstName": "Amy",
        "lastName": "Miller",
        "birthdate": "1992-02-02",
        "email": "amiller@fake.com",
        "phone": "8005554242",
        "street1": "13 School St.",
        "street2": "Apt. 5",
        "city": "Washington",
        "stateProvince": "QC",
        "postalCode": "A1A1A1",
        "country": "Canada"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # POST-запрос на создание второго контакта
    r = requests.post(url_contacts, headers=headers, json=second_contact_payload)
    assert r.status_code == 201, f"Ошибка при создании нового контакта: {r.status_code} {r.text}"
    contact_id = r.json()["_id"]

    # Сохраняем ID второго контакта
    contact_ids = {}
    if os.path.exists(contact_ids_file):
        with open(contact_ids_file, 'r', encoding='utf-8') as f:
            contact_ids = json.load(f)

    contact_ids["second_contact_id"] = contact_id

    with open(contact_ids_file, 'w', encoding='utf-8') as f:
        json.dump(contact_ids, f, ensure_ascii=False, indent=4)

    # Сохраняем шаблон контакта
    with open(second_template_file, 'w', encoding='utf-8') as f:
        json.dump(second_contact_payload, f, ensure_ascii=False, indent=4)

    print("Второй контакт создан и сохранён.")
