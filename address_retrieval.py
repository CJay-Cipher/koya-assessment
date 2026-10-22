import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_address(lat, lng):
    url = "https://api.apilayer.net/positionstack/v1/reverse"
    params = {
        "access_key": API_KEY,
        "query": f"{lat},{lng}",
        "limit": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not data["data"]:
        print("No address found")
        return None

    return data["data"][0]["label"]


lat = 6.4410
lng = 3.5357

address = get_address(lat, lng)
print(address)
