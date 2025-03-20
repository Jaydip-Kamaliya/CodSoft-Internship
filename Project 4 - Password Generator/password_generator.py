import random

class PasswordGenerator:

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    symbols = "!@#$%^&*"

    def generate_password(self, length=8):
        all_characters = self.uppercase + self.lowercase + self.digits + self.symbols
        password = []
        
        # Ensure the password has at least one uppercase, lowercase, digit, and symbol for better strength
        password.append(random.choice(self.uppercase))
        password.append(random.choice(self.lowercase))
        password.append(random.choice(self.digits))
        password.append(random.choice(self.symbols))

        for i in range (length - 4): # 4 characters already added
            character = random.choice(all_characters)
            password.append(character)

        # Shuffle password to avoid same pattern
        random.shuffle(password)

        # Return password in string format
        return "".join(password)

def main():
    p = PasswordGenerator()
    while True:

        try:
            user_input = input("\nEnter password's expected length (default 8): ")
            
            # Allow user to exit the program
            if user_input.lower() == 'exit':
                break

            # Handle empty input for default length
            if user_input.strip() == "":
                password_length = 8
            else:
                password_length = int(user_input)

            # Check for valid length
            if password_length < 4 or password_length > 16:
                print("Password's length should be between 4 to 16 characters.")
            else:
                print(f"Generated Password: {p.generate_password(password_length)}")
        
        except ValueError:
            print("Please enter a valid number or type 'exit' to quit.")


print("\n====== Password Generator ======\n")
print("Instructions:")
print("- The password length should be between 4 and 16 characters.")
print("- Type 'exit' to terminate the program.")

main()