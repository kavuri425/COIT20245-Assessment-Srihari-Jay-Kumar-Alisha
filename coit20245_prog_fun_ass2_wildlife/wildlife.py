import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
def get_species_list(coordinate, radius):
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={coordinate['latitude']},{coordinate['longitude']},{radius}"
    response = requests.get(url=url, headers=headers)
    data = response.json()['SpeciesSightingSummariesContainer']['SpeciesSightingSummary']
    return [species['Species'] for species in data]

def get_surveys_by_species(coordinate, radius, taxonid):
    url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&&circle={coordinate['latitude']},{coordinate['longitude']},{radius}"
    response = requests.get(url=url, headers=headers)
    data = response.json()['features']
    return [sighting['properties'] for sighting in data if sighting['properties'].get('SiteCode') == 'INCIDENTAL']

# Add assert statements for testing
def test_get_species_list():
    coords = {"latitude": -16.92, "longitude": 145.777}
    species_list = get_species_list(coords, 100000)
    assert isinstance(species_list, list)
    assert len(species_list) > 0

def test_get_surveys_by_species():
    coords = {"latitude": -16.92, "longitude": 145.777}
    surveys = get_surveys_by_species(coords, 100000, 860)
    assert isinstance(surveys, list)
    assert len(surveys) > 0

if __name__ == "__main__":
    test_get_species_list()
    test_get_surveys_by_species()
    print("All tests passed.")
