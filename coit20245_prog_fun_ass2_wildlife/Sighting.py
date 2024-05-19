import nominatim
import wildlife
import requests

def safe_get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

def display_menu():
    print("Help")
    print("====")
    print("The following commands are recognised.")
    print("Display help                       wildlife> help")
    print("Exit the application               wildlife> exit")
    print("Display animal species in a city   wildlife> species Brisbane")
    print("Display animal sightings in a city wildlife> sightings Brisbane 15255")
    print("Display venomous species           wildlife> species Brisbane venomous")

def main():
    display_menu()
    while True:
        command = input("wildlife> ")
        if command == "help":
            display_menu()
        elif command == "exit":
            break
        elif command.startswith("species "):
            parts = command.split(" ")
            city = parts[1]
            if len(parts) > 2 and parts[2] == "venomous":
                species_list = search_species(city)
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species)
            else:
                species_list = search_species(city)
                display_species(species_list)
        elif command.startswith("sightings "):
            parts = command.split(" ")
            if len(parts) < 3:
                print("Error: The 'sightings' command requires a city and a taxonid.")
            else:
                city = parts[1]
                taxonid = parts[2]
                sightings = search_sightings(taxonid, city)
                display_sightings(sightings)
        else:
            print("Invalid command. Type 'help' for available commands.")

def search_species(city):
    coordinate = gps(city)
    radius = 100000
    return wildlife.get_species_list(coordinate, radius)

def display_species(species_list):
    for species in species_list:
        print(f"{safe_get(species, 'AcceptedCommonName')} - {safe_get(species, 'PestStatus') or 'Unknown'}")

def search_sightings(taxonid, city):
    coordinate = gps(city)
    radius = 100000
    return wildlife.get_surveys_by_species(coordinate, radius, taxonid)

def display_sightings(sightings):
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        print(f"Sighting Date: {safe_get(sighting, 'StartDate')}, Location: {safe_get(sighting, 'LocalityDetails')}")

def filter_venomous(species_list):
    return [species for species in species_list if safe_get(species, 'PestStatus') == "Venomous"]

def gps(city):
    print(nominatim.gps_coordinate(city))
    return nominatim.gps_coordinate(city)
  

def earliest(sightings):
    return min(sightings, key=lambda x: safe_get(x, 'StartDate'))

def sort_by_date(sightings):
    return sorted(sightings, key=lambda x: safe_get(x, 'StartDate'))

if __name__ == "__main__":
    main()


