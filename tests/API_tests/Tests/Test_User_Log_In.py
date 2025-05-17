import requests
import pytest
import json
import os


@pytest.mark.login
def test_user_login():
    url = "https://thinking-tester-contact-list.herokuapp.com/users/login"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    user_file = os.path.join(current_dir, "..", "Test_Data", "create_user_template.json")
    user_file = os.path.normpath(user_file)

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
            with open("token.json", "w", encoding="utf-8") as f:
                f.write(json.dumps({"token": token}))
            print("Токен успешно сохранён в token.json")
        except Exception as e:
            print("Ошибка обработки токена:", e)
    else:
        print("Ошибка авторизации!")
