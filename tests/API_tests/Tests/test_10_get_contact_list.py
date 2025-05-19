import pytest
import requests
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.get_contact_list
def test_get_contact_list(read_config):
    url = f"{read_config['URL']}/contacts"
    token = load_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    print("GET Contact List response:", response.status_code)
    print("Response body:", response.text)

    assert response.status_code == 200, "Не удалось получить список контактов"
    contacts = response.json()
    assert isinstance(contacts, list), "Ответ не является списком контактов"
    assert len(contacts) > 0, "Список контактов пуст"
