import requests
import json
import os

AUTH_URL = "https://thinking-tester-contact-list.herokuapp.com/users/login"

# Абсолютный путь к token.json
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_PATH = os.path.join(CURRENT_DIR, "token.json")

# Абсолютный путь к create_user_template.json
USER_TEMPLATE_PATH = os.path.join(CURRENT_DIR, "create_user_template.json")


def load_user_credentials():
    with open(USER_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["email"], data["password"]


def get_auth_token():
    """
    Получает токен через API и перезаписывает token.json.
    """
    email, password = load_user_credentials()
    payload = {"email": email, "password": password}

    response = requests.post(AUTH_URL, json=payload)
    assert response.status_code == 200, f"Ошибка: ожидался код 200, получили {response.status_code}"

    token = response.json()["token"]

    with open(TOKEN_PATH, "w", encoding="utf-8") as f:
        json.dump({"token": token}, f, ensure_ascii=False, indent=4)

    return token


def load_token():
    """
    Загружает токен из файла или запрашивает новый, если файл отсутствует или повреждён.
    """
    try:
        with open(TOKEN_PATH, "r", encoding="utf-8") as f:
            return json.load(f)["token"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        return get_auth_token()