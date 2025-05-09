import requests

url = "https://thinking-tester-contact-list.herokuapp.com/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
