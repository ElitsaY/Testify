import requests

url = "http://127.0.0.1:8000/accounts/register/"
data = {
    "username": "student1",
    "email": "student1@example.com",
    "password": "someStrongP4ss",
    "faculty_number": "12345"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
