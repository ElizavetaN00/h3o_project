import pytest
import requests
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config


@pytest.mark.logout
def test_user_logout(read_config):
    url = f"{read_config['URL']}/users/logout"

    token = load_token()

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
