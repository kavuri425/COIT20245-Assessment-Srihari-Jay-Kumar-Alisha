import os

def display_menu():
    print("Welcome to Wildlife Sighting Tracker!")
    print("===================================")
    print("a. Print help menu")
    print("b. Exit the program")

def create_project_folder():
    folder_name = "coit20245_prog_fun_ass2_wildlife"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created project folder: {folder_name}")
    else:
        print("Project folder already exists.")

if __name__ == "__main__":
    create_project_folder()
    
    # Debugging display_menu() function
    display_menu()

    while True:
        choice = input("Enter your choice (a/b): ").strip().lower()

        if choice == 'a':
            print("Help menu:")
            print("This program helps you track wildlife sightings.")
        elif choice == 'b':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'a' or 'b'.")

