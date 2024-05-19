import requests

def gps_coordinate(city):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url=url, headers=headers)
    data = response.json()[0]
    return {"latitude": float(data['lat']), "longitude": float(data['lon'])}

# Add assert statements for testing 
def test_gps_coordinate():
    brisbane_coords = gps_coordinate("Brisbane")
    assert isinstance(brisbane_coords, dict)
    assert 'latitude' in brisbane_coords and 'longitude' in brisbane_coords

if __name__ == "__main__":
    test_gps_coordinate()
    print("All tests passed.")
