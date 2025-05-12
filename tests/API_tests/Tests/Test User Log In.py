import requests
import pytest
import json


@pytest.mark.login
def test_user_login():
    url = "https://thinking-tester-contact-list.herokuapp.com/users/login"

    payload = {
        "email": "testmailforzv123@fake.com",
        "password": "myNewPazzword"
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        try:
            token = response.json()["token"]
            with open("token.json", "w", encoding="utf-8") as f:
                f.write(json.dumps({"token": token}))
            print("Токен успешно сохранён в token.json")
        except Exception as e:
            print("Ошибка обработки токена:", e)
    else:
        print("Ошибка авторизации!")
