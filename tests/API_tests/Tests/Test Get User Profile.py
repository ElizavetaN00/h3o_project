import json
import pytest
import requests
from tests.API_tests.conftest import read_config

@pytest.mark.get_user_profile
def test_get_user_profile(read_config):
    url = f"{read_config['URL']}/me"

    # Читаем токен из файла
    with open("token.json", "r", encoding="utf-8") as f:
        token = json.load(f)["token"]

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print(response.text)
