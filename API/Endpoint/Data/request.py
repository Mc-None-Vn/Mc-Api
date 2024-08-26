import requests

url = "https://example.com/api/data"
data = {"name": "John", "age": 30}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Data has been saved successfully")
else:
    print("Error saving data")
