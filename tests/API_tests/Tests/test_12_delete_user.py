import pytest
import requests
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.delete_user
def test_delete_user(read_config):
    url_delete = f"{read_config['URL']}/users/me"

    token = load_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.delete(url_delete, headers=headers)

    assert response.status_code == 200, f"Ошибка удаления: {response.status_code} {response.text}"
    assert not response.text, "Ответ должен быть пустым"
