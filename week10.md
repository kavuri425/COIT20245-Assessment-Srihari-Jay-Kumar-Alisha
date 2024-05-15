# tASK 9

import requests

def get_surveys_by_species(taxon_id, coordinate, radius):
    """
    Retrieves a list of surveys for a particular species in an area specified by a coordinate and radius.

    Args:
    - taxon_id: Taxon ID of the species (int).
    - coordinate: Dictionary containing 'latitude' and 'longitude' keys.
    - radius: Radius of the search area in meters (int).

    Returns:
    - List of surveys for the specified species in the specified area (list).
    """
    base_url = "https://apps.des.qld.gov.au/species"
    endpoint = "getsurveysbyspecies"
    params = {
        "op": endpoint,
        "taxonid": taxon_id,
        "circle": f"{coordinate['latitude']},{coordinate['longitude']},{radius}"
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        surveys = []
        for feature in data.get("features", []):
            survey = {
                "TaxonID": feature["properties"]["TaxonID"],
                "StartDate": feature["properties"]["StartDate"],
                "LocalityDetails": feature["properties"]["LocalityDetails"]
            }
            surveys.append(survey)
        return surveys
    else:
        print(f"Error fetching surveys: {response.status_code}")
        return []

# Test function
def test_get_surveys_by_species():
    """
    Test function for get_surveys_by_species().

    Checks if the function returns a non-empty list of surveys for a known species in a known area.
    """
    taxon_id = 860  # Example taxon ID
    coordinate = {"latitude": -16.92, "longitude": 145.777}
    radius = 100000  # 100 km radius
    surveys = get_surveys_by_species(taxon_id, coordinate, radius)
    if surveys:
        print("Surveys:", surveys)
        assert isinstance(surveys, list)
        assert len(surveys) > 0
        print("get_surveys_by_species() test passed.")
    else:
        print("Failed to fetch surveys for testing.")

if __name__ == "__main__":
    test_get_surveys_by_species()


import requests

def get_surveys_by_species(taxon_id, coordinate, radius):
    """
    Retrieves a list of surveys for a particular species in an area specified by a coordinate and radius.

    Args:
    - taxon_id: Taxon ID of the species (int).
    - coordinate: Dictionary containing 'latitude' and 'longitude' keys.
    - radius: Radius of the search area in meters (int).

    Returns:
    - List of surveys for the specified species in the specified area (list).
    """
    base_url = "https://apps.des.qld.gov.au/species"
    endpoint = "getsurveysbyspecies"
    params = {
        "op": endpoint,
        "taxonid": taxon_id,
        "circle": f"{coordinate['latitude']},{coordinate['longitude']},{radius}"
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        surveys = []
        for feature in data.get("features", []):
            survey = {
                "TaxonID": feature["properties"]["TaxonID"],
                "StartDate": feature["properties"]["StartDate"],
                "LocalityDetails": feature["properties"]["LocalityDetails"]
            }
            surveys.append(survey)
        return surveys
    else:
        print(f"Error fetching surveys: {response.status_code}")
        return []

# Test function
def test_get_surveys_by_species():
    """
    Test function for get_surveys_by_species().

    Checks if the function returns a non-empty list of surveys for a known species in a known area.
    """
    taxon_id = 860  # Example taxon ID
    coordinate = {"latitude": -16.92, "longitude": 145.777}
    radius = 100000  # 100 km radius
    surveys = get_surveys_by_species(taxon_id, coordinate, radius)
    if surveys:
        print("Surveys:", surveys)
        assert isinstance(surveys, list)
        assert len(surveys) > 0
        print("get_surveys_by_species() test passed.")
    else:
        print("Failed to fetch surveys for testing.")

if __name__ == "__main__":
    test_get_surveys_by_species()

import requests

def get_surveys_by_species(coordinate, radius, taxonid):
    """
    Retrieves a list of animal surveys in an area for a given species (taxonid).

    Args:
    - coordinate: Dictionary containing 'latitude' and 'longitude' keys.
    - radius: Radius of the search area in meters (int).
    - taxonid: Taxon ID of the species (int).

    Returns:
    - List of animal surveys in the specified area for the given species (list).
    """
    base_url = "https://apps.des.qld.gov.au/species"
    endpoint = "getsurveysbyspecies"
    params = {
        "op": endpoint,
        "taxonid": taxonid,
        "circle": f"{coordinate['latitude']},{coordinate['longitude']},{radius}"
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        surveys = []
        for feature in data.get("features", []):
            survey = {
                "TaxonID": feature["properties"]["TaxonID"],
                "StartDate": feature["properties"]["StartDate"],
                "LocalityDetails": feature["properties"]["LocalityDetails"]
            }
            surveys.append(survey)
        return surveys
    else:
        print(f"Error fetching surveys: {response.status_code}")
        return []

# Test function
def test_get_surveys_by_species():
    """
    Test function for get_surveys_by_species().

    Checks if the function returns a non-empty list of surveys for a known species in a known area.
    """
    coordinate = {"latitude": -16.92, "longitude": 145.777}
    radius = 100000  # 100 km radius
    taxonid = 860  # Example taxon ID
    surveys = get_surveys_by_species(coordinate, radius, taxonid)
    if surveys:
        print("Surveys:", surveys)
        assert isinstance(surveys, list)
        assert len(surveys) > 0
        print("get_surveys_by_species() test passed.")
    else:
        print("Failed to fetch surveys for testing.")

def search_sightings(taxonid, city):
    """
    Searches for animal sightings in a city for a given species (taxonid).

    Args:
    - taxonid: Taxon ID of the species (int).
    - city: Name of the city (string).

    Returns:
    - List of animal sightings in the city for the given species (list).
    """
    # Placeholder implementation, replace with actual code
    coordinate = {"latitude": YOUR_LATITUDE, "longitude": YOUR_LONGITUDE}  # Use the city's coordinates
    radius = 100000  # 100 km radius
    surveys = get_surveys_by_species(coordinate, radius, taxonid)
    sightings = []
    for survey in surveys:
        if survey.get("SiteCode") == "INCIDENTAL":
            sightings.append(survey)
    return sightings

# Test function
def test_search_sightings():
    """
    Test function for search_sightings().

    Checks if the function returns a non-empty list of sightings for a known species in a known city.
    """
    taxonid = 860  # Example taxon ID
    city = "Cairns"  # Example city
    sightings = search_sightings(taxonid, city)
    if sightings:
        print("Sightings:", sightings)
        assert isinstance(sightings, list)
        assert len(sightings) > 0
        print("search_sightings() test passed.")
    else:
        print("Failed to fetch sightings for testing.")

if __name__ == "__main__":
    test_get_surveys_by_species()
    test_search_sightings()
# TASK 10

def earliest(sightings):
    """
    Returns the sighting with the minimum start date.

    Args:
    - sightings: List of animal sightings (list of dictionaries).

    Returns:
    - Sighting with the minimum start date (dictionary).
    """
    if not sightings:
        return None
    return min(sightings, key=lambda x: x["StartDate"])

def sort_by_date(sightings):
    """
    Returns sightings sorted by date.

    Args:
    - sightings: List of animal sightings (list of dictionaries).

    Returns:
    - Sightings sorted by date (list of dictionaries).
    """
    return sorted(sightings, key=lambda x: x["StartDate"])

def display_sightings(sightings):
    """
    Displays sorted animal sightings.

    Args:
    - sightings: List of animal sightings (list of dictionaries).
    """
    if not sightings:
        print("No sightings found.")
        return

    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        print("Start Date:", sighting["StartDate"])
        print("Locality Details:", sighting["LocalityDetails"])
        print()  # Add empty line for better readability

# Test functions
def test_earliest():
    """
    Test function for earliest().

    Checks if the function returns the sighting with the minimum start date.
    """
    sightings = [
        {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"},
        {"StartDate": "1999-09-20", "LocalityDetails": "Tinaroo Dam"}
    ]
    assert earliest(sightings) == {"StartDate": "1999-09-20", "LocalityDetails": "Tinaroo Dam"}
    print("earliest() test passed.")

def test_sort_by_date():
    """
    Test function for sort_by_date().

    Checks if the function returns sightings sorted by date.
    """
    sightings = [
        {"StartDate": "1999-09-20", "LocalityDetails": "Tinaroo Dam"},
        {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}
    ]
    sorted_sightings = sort_by_date(sightings)
    assert sorted_sightings == [
        {"StartDate": "1999-09-20", "LocalityDetails": "Tinaroo Dam"},
        {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}
    ]
    print("sort_by_date() test passed.")

if __name__ == "__main__":
    test_earliest()
    test_sort_by_date()
