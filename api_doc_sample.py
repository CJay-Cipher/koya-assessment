import requests

url = "https://api.apilayer.net/positionstack/v1/forward"
params = {
    "access_key": "e5288d1bd4471718e266d537b0bff738",
    "query": "1600 Pennsylvania Ave NW, Washington, DC",
    "country": "US,CA",
    "limit": "10",
    "language": "en",
    "output": "json"
}

response = requests.get(url, params=params)
print(response.json())