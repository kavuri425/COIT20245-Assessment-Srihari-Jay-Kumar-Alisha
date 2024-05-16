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
    def display_menu():

     menu = ""


     print(menu)

def main():
    display_menu()
    
    while True:
        command = input("wildlife> ").strip().lower()
        
        if command == "help":
            display_menu()
        elif command == "list":
            print("Listing all tracked animals...")
        elif command == "add":
            print("Adding a new animal...")
        elif command == "remove":
            print("Removing an animal...")

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid command. Type 'help' to see the list of available commands.")

if __name__ == "__main__":
    main()
#Task 2 Input user#

 