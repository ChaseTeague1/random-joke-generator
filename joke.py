import requests

url = "https://icanhazdadjoke.com/"

headers = {
    'Accept' : 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"{data['joke']}")
else:
    print("Could not fetch request")