import requests

url = "http://192.168.20.90:8000/sitat"
data = {
    "quote": "Du er dårlig til å kaste sten."
}
response = requests.post(url, json=data)
data = response.json()
print(f"{data['message']} - ID:{data['id']}")