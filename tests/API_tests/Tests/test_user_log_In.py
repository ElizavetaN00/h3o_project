import pytest
import requests
from tests.API_tests.conftest import read_config, registered_user, logger


@pytest.mark.login
def test_user_login(read_config, registered_user, logger):
    url = f"{read_config['URL']}/users/login"

    payload = {
        "email": registered_user["email"],
        "password": registered_user["password"]
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)

    json_data = response.json()

    # Проверки
    assert response.status_code == 200, "Логин не удался"
    assert "token" in json_data, "Токен отсутствует в ответе"
    assert isinstance(json_data["token"], str) and len(json_data["token"]) > 10

    logger.info("Авторизация прошла успешно. Получен токен.")
    logger.info(f"Статус: {response.status_code}")
    logger.info(f"Ответ: {response.text}")
