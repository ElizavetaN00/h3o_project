import pytest
import requests
import json
import os
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.get_contact
def test_get_contact(read_config):
    base_url = f"{read_config['URL']}/contacts"

    # Загрузка ID из contact_ids.json
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.normpath(os.path.join(current_dir, '..', 'Test_Data'))
    contact_ids_file = os.path.join(test_data_dir, 'contact_ids.json')

    if not os.path.exists(contact_ids_file):
        pytest.skip("Файл contact_ids.json не найден")

    with open(contact_ids_file, 'r', encoding='utf-8') as f:
        contact_ids = json.load(f)

    contact_id = contact_ids.get("first_contact_id")
    if not contact_id:
        pytest.skip("first_contact_id отсутствует в contact_ids.json")

    url = f"{base_url}/{contact_id}"
    token = load_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    print("GET contact:", response.status_code, response.text)

    assert response.status_code == 200, "Не удалось получить контакт"
    contact = response.json()
    assert contact["_id"] == contact_id, "ID контакта не совпадает"
    assert "firstName" in contact and "email" in contact, "Некорректная структура ответа"
