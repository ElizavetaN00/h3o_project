import pytest
import requests
from tests.API_tests.conftest import read_config
from tests.API_tests.Test_Data.auth import load_token


@pytest.mark.get_user_profile
def test_get_user_profile(read_config):
    url = f"{read_config['URL']}/me"

    token = load_token()

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print(response.text)
    assert response.status_code == 200
