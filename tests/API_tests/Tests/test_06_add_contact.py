import pytest
import requests
import json
import os
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.add_contact
def test_add_contact(read_config):
    url_contacts = f"{read_config['URL']}/contacts"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.normpath(os.path.join(current_dir, '..', 'Test_Data'))
    contact_ids_file = os.path.join(test_data_dir, 'contact_ids.json')
    first_template_file = os.path.join(test_data_dir, 'first_contact_template.json')

    token = load_token()

    contact_payload = {
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "1990-01-01",
        "email": "jdoe@fake.com",
        "phone": "1234567890",
        "street1": "123 Main St.",
        "street2": "",
        "city": "New York",
        "stateProvince": "NY",
        "postalCode": "10001",
        "country": "USA"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    contact_ids = {}
    if os.path.exists(contact_ids_file):
        with open(contact_ids_file, 'r', encoding='utf-8') as f:
            contact_ids = json.load(f)

    r = requests.post(url_contacts, headers=headers, json=contact_payload)
    assert r.status_code == 201, f"Не удалось создать контакт: {r.status_code}, {r.text}"

    response_json = r.json()
    contact_id = response_json["_id"]

    # Сохраняем шаблон
    with open(first_template_file, 'w', encoding='utf-8') as f:
        json.dump(contact_payload, f, ensure_ascii=False, indent=4)

    # Сохраняем ID
    contact_ids["first_contact_id"] = contact_id
    with open(contact_ids_file, 'w', encoding='utf-8') as f:
        json.dump(contact_ids, f, ensure_ascii=False, indent=4)

    print(f"Контакт успешно создан и сохранён в {contact_ids_file}")
