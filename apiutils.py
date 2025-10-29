import requests
def fetch_api_data():
    """fetch all data character data from thrones api"""
    return requests.get("https://thronesapi.com/api/v2/Characters").json()
def fetch_image(name,api_data):
    """return image for a given character name"""
    for item in api_data:
        if itenm['fullName']==name:
            return item['imageUrl']
