def display_menu():
    print("Wildlife Sighting Menu")
    print("a. Print help menu")
    print("b. Exit the program")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'a':
            print("Help Menu: \n - This application allows you to manage wildlife sightings.\n - Use the menu options to navigate.")
        elif choice == 'b':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

 