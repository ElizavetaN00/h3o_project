import pytest
import requests
import json
import os
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.update_contact_patch
def test_update_second_contact_patch(read_config):
    url_base = f"{read_config['URL']}/contacts"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.normpath(os.path.join(current_dir, '..', 'Test_Data'))
    contact_ids_file = os.path.join(test_data_dir, 'contact_ids.json')
    second_template_file = os.path.join(test_data_dir, 'second_contact_template.json')

    token = load_token()

    # Проверка наличия ID
    if not os.path.exists(contact_ids_file):
        pytest.skip("contact_ids.json не найден — сначала создай второй контакт.")

    with open(contact_ids_file, 'r', encoding='utf-8') as f:
        contact_ids = json.load(f)

    contact_id = contact_ids.get("second_contact_id")
    if not contact_id:
        pytest.skip("ID второго контакта не найден — сначала создай второй контакт.")

    patch_payload = {
        "email": "amy.updated@fake.com",
        "phone": "8005559999"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    r_patch = requests.patch(f"{url_base}/{contact_id}", headers=headers, json=patch_payload)
    print("PATCH response:", r_patch.status_code, r_patch.text)
    assert r_patch.status_code == 200, f"PATCH update failed: {r_patch.status_code} {r_patch.text}"

    updated_contact = r_patch.json()
    with open(second_template_file, 'w', encoding='utf-8') as f:
        json.dump(updated_contact, f, ensure_ascii=False, indent=4)

    print("Второй контакт успешно обновлён.")
