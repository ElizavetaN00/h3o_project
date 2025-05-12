import requests
import json

AUTH_URL = "https://thinking-tester-contact-list.herokuapp.com/users/login"


def get_auth_token(email="testmailforzv@fake.com", password="myPazzword"):
    payload = {"email": email, "password": password}

    response = requests.post(AUTH_URL, json=payload)
    assert response.status_code == 200, f"Ошибка: ожидался код 200, получили {response.status_code}"

    token = response.json()["token"]

    # Сохраняем токен в файл для повторного использования
    with open("token.json", "w", encoding="utf-8") as f:
        f.write(json.dumps({"token": token}))

    return token


def load_token():
    try:
        with open("token.json", "r") as f:
            return json.load(f)["token"]
    except (FileNotFoundError, KeyError):
        return get_auth_token()  # Если файла нет, получаем новый токен
