import sys
from Database import DBhelper


class Daraz:
    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        Welcome to Daraz!
        Please choose an option:
        1. Register
        2. Login 

        Enter your choice: 
        """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            print("Invalid input. Please try again.")
            sys.exit(1000)

    def register(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        response = self.db.register(name, email, password)

        if response == 1:
            print("Registration Successful")
        else:
            print("Registration Failed")

        self.menu()

    def login(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        data = self.db.search(email, password)

        if len(data) == 0:
            print("Incorrect Credentials")
            self.login()
        else:
            print("Login Successful")
            print("Hello", data[0][1], "!!!")
            self.login_menu(email)

    def login_menu(self, email):
        while True:
            user_input = input("""
            1. See Profile
            2. Edit Profile
            3. Delete Profile
            4. Logout

            Enter your choice: 
            """)

            if user_input == "1":
                self.view_profile(email)
            elif user_input == "2":
                self.edit_profile(email)
            elif user_input == "3":
                self.delete_profile(email)
                break
            elif user_input == "4":
                print("Logged out successfully.")
                self.menu()
                break
            else:
                print("Invalid input. Please try again.")

    def view_profile(self, email):
        profile = self.db.get_profile(email)
        if profile:
            print("\nProfile Details:")
            print(f"Name: {profile[1]}")
            print(f"Email: {profile[2]}")
            print(f"Password: {profile[3]}\n")
        else:
            print("Unable to retrieve profile details.")

    def edit_profile(self, email):
        name = input("Enter new name: ")
        new_email = input("Enter new email: ")
        password = input("Enter new password: ")

        response = self.db.update_profile(name, new_email, password)

        if response == 1:
            print("Profile updated successfully.")
        else:
            print("Failed to update profile. Please try again.")

    def delete_profile(self, email):
        confirmation = input("Are you sure you want to delete your profile? (yes/no): ").lower()
        if confirmation == "yes":
            response = self.db.delete_profile(email)
            if response == 1:
                print("Profile deleted successfully.")
                self.menu()
            else:
                print("Failed to delete profile. Please try again.")
        else:
            print("Profile deletion canceled.")


obj = Daraz()
