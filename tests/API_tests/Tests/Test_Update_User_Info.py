import pytest
import requests
import json
import os


@pytest.mark.update_user_info
def test_update_user_info():
    url_login = "https://thinking-tester-contact-list.herokuapp.com/users/login"
    url_patch = "https://thinking-tester-contact-list.herokuapp.com/users/me"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    user_file = os.path.join(current_dir, '..', 'Test_Data', 'create_user_template.json')
    user_file = os.path.normpath(user_file)

    with open(user_file, 'r', encoding='utf-8') as file:
        user_data = json.load(file)

    login_payload = {
        "email": user_data["email"],
        "password": user_data["password"]
    }

    r = requests.post(url_login, json=login_payload)
    print("Login:", r.status_code, r.text)
    assert r.status_code == 200, f"Login failed: {r.status_code} {r.text}"

    token = r.json()["token"]

    new_password = "myPazzword_NEW123"
    patch_payload = {
        "firstName": "Updated",
        "lastName": "Username",
        "email": user_data["email"],
        "password": new_password
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    r = requests.patch(url_patch, headers=headers, json=patch_payload)
    print("PATCH:", r.status_code, r.text)
    assert r.status_code == 200, f"PATCH failed: {r.status_code} {r.text}"

    user_data.update(patch_payload)
    with open(user_file, 'w', encoding='utf-8') as file:
        json.dump(user_data, file, ensure_ascii=False, indent=4)
    print("Файл успешно обновлён.")
