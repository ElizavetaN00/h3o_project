import requests
import pytest
import json
from tests.API_tests.Helper.send_r import send_request


@pytest.mark.add_user
def test_add_user(read_config, read_cut):
    url = f"{read_config['URL']}/users"
    payload = read_cut
    response = send_request("POST", url, json=payload)
    print(f"Ответ сервера: {response}")
    token = response["token"]
    with open("token.json", "w", encoding="utf-8") as f:
        f.write(json.dumps({"token": token}))
    headers = {
      'Content-Type': 'application/json',
      'Cookie': f'token={token}'
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text)
