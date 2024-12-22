import requests


api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0ODk1ODg0LCJpYXQiOjE3MzQ4OTU1ODQsImp0aSI6ImU5ZjhjMTVlMzY4NzQxZWM4ZjMyZjc5MDI5MGQxNmVjIiwidXNlcl9pZCI6MX0.fWdswHcZxfvoHnr3_p54V4eq88brClK9BdSJFkxHlJY"
url = "http://127.0.0.1:8000/accounts/create_teacher/"
data = {
    "username": "teacher1",
    "email": "teacher1@example.com",
    "password": "teach123",
    "role": "teacher"
}
headers = {"Content-Type": "application/json", 
           "Authorization": f"Bearer {api_key}"}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
