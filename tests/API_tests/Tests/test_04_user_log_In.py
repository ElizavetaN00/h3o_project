import requests
import pytest
import json
import os
from tests.API_tests.conftest import read_config


@pytest.mark.login
def test_user_login(read_config):
    url = f"{read_config['URL']}/users/login"

    # Путь к файлу с данными пользователя
    current_dir = os.path.dirname(os.path.abspath(__file__))
    user_file = os.path.normpath(os.path.join(current_dir, "..", "Test_Data", "create_user_template.json"))

    with open(user_file, 'r', encoding='utf-8') as file:
        user_data = json.load(file)

    payload = {
        "email": user_data["email"],
        "password": user_data["password"]
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        try:
            token = response.json()["token"]

            # Сохраняем токен в Test_Data/token.json
            token_file = os.path.normpath(os.path.join(current_dir, "..", "Test_Data", "token.json"))
            with open(token_file, "w", encoding="utf-8") as f:
                json.dump({"token": token}, f)

            print(f"Токен успешно сохранён в {token_file}")
        except Exception as e:
            print("Ошибка обработки токена:", e)
    else:
        print("Ошибка авторизации!")
