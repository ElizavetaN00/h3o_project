import requests
import pytest
import json
import os
from tests.API_tests.conftest import read_config, read_cut


@pytest.mark.add_user
def test_add_user(read_config, read_cut):
    url = f"{read_config['URL']}/users"
    payload = read_cut

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)

    print(f"Ответ сервера: {response.status_code} {response.text}")

    # Проверка успешной регистрации
    assert response.status_code == 201, f"Регистрация не удалась: {response.status_code} {response.text}"

    # Получаем и сохраняем токен
    json_response = response.json()
    assert "token" in json_response, "Токен не вернулся в ответе"

    token = json_response["token"]

    # Путь к файлу token.json (в той же папке где находится read_cut — Test_Data)
    test_data_dir = os.path.dirname(os.path.abspath(__file__)).replace("Tests", "Test_Data")
    token_path = os.path.join(test_data_dir, "token.json")

    with open(token_path, "w", encoding="utf-8") as f:
        json.dump({"token": token}, f)

    print(f"Токен сохранён в {token_path}")
