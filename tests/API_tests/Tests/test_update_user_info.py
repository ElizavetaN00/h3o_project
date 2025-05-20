import pytest
import requests
from tests.API_tests.conftest import read_config, auth_token, registered_user, logger


@pytest.mark.update_user_info
def test_update_user_info(read_config, auth_token, registered_user, logger):
    url = f"{read_config['URL']}/users/me"

    new_password = "UpdatedPass456!"
    updated_payload = {
        "firstName": "Updated",
        "lastName": "User",
        "email": registered_user["email"],
        "password": new_password
    }

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    response = requests.patch(url, headers=headers, json=updated_payload)

    json_data = response.json()

    # Проверки
    assert response.status_code == 200
    assert json_data["firstName"] == "Updated"
    assert json_data["lastName"] == "User"

    logger.info(f"Данные пользователя обновлены: статус {response.status_code}, ответ: {response.text}")
