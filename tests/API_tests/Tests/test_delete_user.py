import pytest
import requests
from tests.API_tests.conftest import read_config, registered_user, logger


@pytest.mark.delete_user
def test_delete_user(read_config, registered_user, logger):
    base_url = read_config['URL']

    # Шаг 1: логин и получение токена на основе registered_user
    login_payload = {
        "email": registered_user["email"],
        "password": registered_user["password"]
    }

    r_login = requests.post(f"{base_url}/users/login", json=login_payload)
    assert r_login.status_code == 200, f"Авторизация не удалась: {r_login.status_code} {r_login.text}"
    token = r_login.json().get("token")
    assert token, "Токен не получен"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Шаг 2: удаление пользователя
    r_delete = requests.delete(f"{base_url}/users/me", headers=headers)
    assert r_delete.status_code == 200, f"Удаление не удалось: {r_delete.status_code} {r_delete.text}"
    assert r_delete.text.strip() == "", "Ответ при удалении должен быть пустым"

    logger.info("Пользователь успешно удалён.")
    logger.info(f"Cтатус: {r_delete.status_code}")
