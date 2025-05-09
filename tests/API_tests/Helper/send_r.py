import requests


def send_request(method, url, headers=None, params=None, data=None, json=None):
    response = requests.request(method, url, headers=headers, params=params, data=data, json=json)

    return response.json()