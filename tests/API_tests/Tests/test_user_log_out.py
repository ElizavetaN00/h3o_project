import pytest
import requests
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger


@pytest.mark.logout
def test_user_logout(read_config, auth_token, registered_user, logger):
    url = f"{read_config['URL']}/users/logout"

    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers)

    # Проверки
    assert response.status_code == 200
    assert response.text.strip() == ""  # тело ответа должно быть пустым

    logger.info(f"Статус: {response.status_code}")
    logger.info(f"Ответ: '{response.text}'")

