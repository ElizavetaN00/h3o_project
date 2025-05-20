import pytest
import requests
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger


@pytest.mark.get_user_profile
def test_get_user_profile(read_config, auth_token, registered_user, logger):
    url = f"{read_config['URL']}/users/me"

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    # Проверки
    assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
    assert "firstName" in data, "Поле firstName отсутствует"
    assert "email" in data, "Поле email отсутствует"

    logger.info(f"Статус: {response.status_code}")
    logger.info(f"Получены данные пользователя: {data}")
