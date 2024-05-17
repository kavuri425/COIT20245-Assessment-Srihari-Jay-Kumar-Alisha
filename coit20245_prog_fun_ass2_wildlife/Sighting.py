import nominatim
import wildlife
import requests

def display_menu():
    print("Help")
    print("====")
    print("The following commands are recognised.")
    print("Display help                       wildlife> help")
    print("Exit the application               wildlife> exit")
    print("Display animal species in a city   wildlife> species <city>")
    print("Display animal sightings in a city wildlife> sightings <city> <taxonid>")
    print("Display venomous species           wildlife> species <city> venomous")

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
        print(f"{species['AcceptedCommonName']} - {species.get('PestStatus', 'Unknown')}")

def search_sightings(taxonid, city):
    coordinate = gps(city)
    radius = 100000
    return wildlife.get_surveys_by_species(coordinate, radius, taxonid)

def display_sightings(sightings):
    sorted_sightings = sort_by_date(sightings)
    for sighting in sorted_sightings:
        print(f"Sighting Date: {sighting['StartDate']}, Location: {sighting['LocalityDetails']}")

def filter_venomous(species_list):
    return [species for species in species_list if species.get('PestStatus') == "Venomous"]

def gps(city):
    return nominatim.gps_coordinate(city)

def earliest(sightings):
    return min(sightings, key=lambda x: x['StartDate'])

def sort_by_date(sightings):
    return sorted(sightings, key=lambda x: x['StartDate'])

if __name__ == "__main__":
    main()