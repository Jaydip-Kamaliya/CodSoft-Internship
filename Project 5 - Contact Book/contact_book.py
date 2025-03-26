import sqlite3

class ContactBook:

    def __init__(self, db_path="contacts.db"):
        self.db_path = db_path
        self.setup_database()

    def setup_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Creates a 'contacts' table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    number TEXT
                )''')

            conn.commit()

    def add_contact(self, name, number):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Check if the number already exists
            cursor.execute("SELECT * FROM contacts WHERE number = ?", (number,))
            existing_contact = cursor.fetchone()

            if existing_contact:
                print("\nError: This number is already saved under another contact!")
                return

            cursor.execute("INSERT INTO contacts(name, number) VALUES (?, ?)", (name, number))          
            conn.commit()
            print("The contact has been added successfully!")

    def view_contacts(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM contacts")
            contacts = cursor.fetchall()

            if not contacts:
                print("\nNo saved contacts")
                return False
            
            print("\n{:<3} | {:<20} | {:<15}".format("ID", "Name", "Number"))
            print("-"*46)
            
            for contact in contacts:
                contact_id, name, number = contact
                print(f"{contact_id:<3} | {name:<20} | {number:<15}")

            print()
            return len(contacts) # To use it in subsequent functions.
         
    def update_contact(self):
        total_contacts = self.view_contacts()

        if total_contacts:
            update_id = input("Enter the Contact ID you want to update: ")
            
            # Validate the entered Contact ID.
            if update_id.isdigit() and int(update_id) <= total_contacts and int(update_id) > 0:

                print()
                print("1. Update Name")
                print("2. Update Number")

                update_choice = input("\nEnter your choice (1 or 2): ")

                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()

                    # Update Name
                    if update_choice == "1":
                        update_name = input("\nEnter the new Name: ")
                        cursor.execute("UPDATE contacts SET name = ? WHERE id = ?", (update_name, update_id))
                        conn.commit()
                        print("The name has been updated!")

                    # Update Number
                    elif update_choice == "2":
                        update_number = input("\nEnter the new Number: ")

                        # Check if entered number is valid
                        if len(update_number) == 10 and update_number.isdigit():
                            cursor.execute("UPDATE contacts SET number = ? WHERE id = ?", (update_number, update_id))
                            conn.commit()
                            print("The number has been updated!")
                        else:
                            print("\nError : The phone number must be 10 digits. Please try again!")

                    else:
                        print("Please enter a valid choice (1 or 2)")

            else:
                print("Error : Invalid Contact ID. Please try again")

    def delete_contact(self):
        total_contacts = self.view_contacts()

        if total_contacts:
            delete_id = input("Enter the Contact ID you want to delete: ")

            # Validate the entered Contact ID.
            if delete_id.isdigit() and int(delete_id) <= total_contacts and int(delete_id) > 0:

                with sqlite3.connect(self.db_path) as conn:
                    cursor = conn.cursor()

                    # Delete the contact
                    cursor.execute("DELETE FROM contacts WHERE id = ?", (delete_id,))
                    conn.commit()
                    print("The contact has been deleted!")

                    # Reorder IDs after deletion
                    cursor.execute("UPDATE contacts SET id = id - 1 WHERE id > ?", (delete_id,))
                    conn.commit()

                    # Reset auto-increment to maintain proper ID order
                    cursor.execute("DELETE FROM sqlite_sequence WHERE name='contacts'")
                    conn.commit()                    

            else:
                print("Error : Invalid Contact ID. Please try again")