import requests

def gps_coordinate(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url=url, headers=headers)
    data = response.json()[0]
    return {"latitude": float(data['lat']), "longitude": float(data['lon'])}