import pytest
import requests
import json
import os
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.delete_contact
def test_delete_contact(read_config):
    url_base = f"{read_config['URL']}/contacts"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.normpath(os.path.join(current_dir, '..', 'Test_Data'))
    contact_ids_file = os.path.join(test_data_dir, 'contact_ids.json')

    token = load_token()

    # Загружаем ID контакта
    with open(contact_ids_file, 'r', encoding='utf-8') as f:
        contact_ids = json.load(f)
        contact_id = contact_ids.get("first_contact_id")
        assert contact_id, "first_contact_id не найден в contact_ids.json"

    url_delete = f"{url_base}/{contact_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Удаление контакта
    r = requests.delete(url_delete, headers=headers)
    print("Delete contact:", r.status_code, r.text)
    assert r.status_code == 200, "Контакт не был удалён"

    # Проверка, что контакт действительно удалён
    r_check = requests.get(url_delete, headers=headers)
    assert r_check.status_code in [404, 400], "Контакт всё ещё существует"