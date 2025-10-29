import requests

def fetch_api_data():
    url = "https://thronesapi.com/api/v2/Characters"
    response = requests.get(url)
    return response.json()

def fetch_image(name, api_data):
    for item in api_data:
        if item['fullName'] == name:
            return item['imageUrl']
    return None
