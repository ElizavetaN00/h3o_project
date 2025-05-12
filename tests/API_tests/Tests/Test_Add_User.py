import requests
import pytest
from tests.API_tests.Test_Data.auth import load_token
from tests.API_tests.conftest import read_config, read_cut


@pytest.mark.add_user
def test_add_user(read_config, read_cut):
    url = f"{read_config['URL']}/users"
    payload = read_cut

    token = load_token()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, headers=headers, json=payload)
    print(f"Ответ сервера: {response.status_code} {response.text}")
