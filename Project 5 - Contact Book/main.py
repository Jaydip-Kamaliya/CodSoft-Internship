from contact_book import ContactBook

def main_menu():
    print()
    print("1. Add New Contact")
    print("2. View Contact List")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def valid_choice(input_choice):
    choices = ["1", "2", "3", "4", "5"]

    # If invalid, prints a warning and prevents execution
    if input_choice not in choices:
        print("Please only choose valid Number between 1 to 5")
        return False 
    return True

def main():
    contact = ContactBook()

    while True:
        main_menu()

        choice = input("\nEnter your choice (1-5): ")
        valid_choice(choice)

        if choice == "1":

            # Check if name is not empty
            name = input("Enter Name: ").strip()

            if not name:
                print("\nError : Name cannot be empty")
                continue

            # Check if entered number is valid
            number = input("Enter Number: ")
            
            if len(number) == 10 and number.isdigit():
                contact.add_contact(name, number)
            else:
                print("\nError : The phone number must be 10 digits. Please try again!")

        elif choice == "2":
            contact.view_contacts()

        elif choice == "3":
            contact.update_contact()

        elif choice == "4":
            contact.delete_contact()

        elif choice == "5":
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)