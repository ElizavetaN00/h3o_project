import pytest
import requests
from tests.API_tests.conftest import read_config, auth_token, created_contact_id, registered_user, logger


@pytest.mark.get_contact
def test_get_contact(read_config, auth_token, created_contact_id, registered_user, logger):
    url = f"{read_config['URL']}/contacts/{created_contact_id}"

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.get(url, headers=headers)

    contact = response.json()

    # Проверки
    assert response.status_code == 200, "Не удалось получить контакт"
    assert contact["_id"] == created_contact_id, "ID контакта не совпадает"
    assert "firstName" in contact and "email" in contact, "Некорректная структура ответа"

    logger.info(f"Контакт получен: {response.text}")
    logger.info(f"Статус: {response.status_code}")

