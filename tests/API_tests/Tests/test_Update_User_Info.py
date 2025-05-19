import pytest
import requests
import json
import os
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.update_user_info
def test_update_user_info(read_config):
    url_patch = f"{read_config['URL']}/users/me"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.normpath(os.path.join(current_dir, '..', 'Test_Data'))
    user_template_path = os.path.join(test_data_dir, 'create_user_template.json')

    token = load_token()
    if not token:
        pytest.skip("❌ Токен не найден")

    with open(user_template_path, 'r', encoding='utf-8') as f:
        user_data = json.load(f)

    new_password = "NewSecurePassword456"
    update_payload = {
        "firstName": "Updated",
        "lastName": "User",
        "email": user_data["email"],
        "password": new_password
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    r = requests.patch(url_patch, headers=headers, json=update_payload)
    print("PATCH:", r.status_code, r.text)
    assert r.status_code == 200, f"PATCH failed: {r.status_code} {r.text}"

    user_data.update(update_payload)
    with open(user_template_path, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, ensure_ascii=False, indent=4)

    print("Данные пользователя успешно обновлены в create_user_template.json")
