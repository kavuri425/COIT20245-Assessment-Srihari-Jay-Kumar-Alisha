import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
def get_species_list(coordinate, radius):
    url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={coordinate['latitude']},{coordinate['longitude']},{radius}"
    response = requests.get(url=url, headers=headers)
    data = response.json()['SpeciesSightingSummariesContainer']['SpeciesSightingSummary']
    return [species['Species'] for species in data]
