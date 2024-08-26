import requests

url = "https://mc-none-vn.onrender.com/api/data/save"
data = {"name": "Your name", "pw": "Your password"}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Data has been saved successfully")
else:
    print("Error saving data")
