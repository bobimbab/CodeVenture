import re

from user import User, YoungLearner, Admin
from datetime import date
from game import Game
from quizzes import Quizzes


class Interface:
    """
    Interface is a class for managing user interactions and controlling the educational game system.

    Attributes:
        users_dict (dict): A dictionary storing user data.
        current_user (str): Stores the username of the current user.

    Methods:
        __init__(self):
            Initialize a new Interface object and parse user data.

        parse_data(self, file_name):
            Parse user data from a text file and store it in the users_dict attribute.

        is_leap_year(year):
            Check if a given year is a leap year.

        date_value_check(year, month, day):
            Check if a given date is valid.

        ph_num_check(ph_num):
            Validate the length of a phone number.

        email_check(email):
            Validate the format of an email address.

        grade_check(grade):
            Validate the input grade of a young learner's user.

        main_menu(self):
            Display the main menu options.

        login_menu(self):
            Allow users to log into their accounts.

        registration_menu(self):
            Allow users to create a new account.

        reset_password_menu(self):
            Allow users to reset their password.

        admin_interface(self):
            Display the menu options for admin users.

        learners_interface(self):
            Display the menu options for young learner users.
        """

    def __init__(self):
        """
        Initialize a new Interface object and parse user data.
        """
        self.users_dict = dict()
        self.current_user: str = None
        self.parse_data("user_data.txt")

    def parse_data(self, file_name):
        """
        Parse user data from a text file and store it in the users_dict attribute.

        Args:
            file_name (str): The name of the text file containing user data.

        Returns:
            None
        """
        with open(file_name, "r", encoding="utf8") as file:
            try:
                for line in file:
                    line = line.strip()
                    line = line.split(",")

                    if len(line) == 8:
                        user_obj = YoungLearner(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
                        self.users_dict[user_obj.username] = user_obj
                    else:
                        user_obj2 = Admin(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                        self.users_dict[user_obj2.username] = user_obj2
            except:
                print("File cannot be parsed!")

    # ===================================== Validation ===================================== #

    @staticmethod
    def is_leap_year(year):
        """
        Check if a given year is a leap year.

        Args:
            year (int): The year to check.

        Returns:
            bool: True if the year is a leap year, False otherwise.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def date_value_check(year, month, day):
        """
        Check if a given date is valid.

        Args:
            year (int): The year.
            month (int): The month.
            day (int): The day.

        Returns:
            bool: True if the date is valid, False otherwise.
        """

        # Convert to integers
        curr_year = date.today().year
        year_num = int(year)
        month_num = int(month)
        day_num = int(day)

        # Retrieve valid range values
        valid_years = range(1000, curr_year)
        valid_months = range(1, 13)
        if month_num not in valid_months \
                or year_num not in valid_years:
            return False

        # Days of a calendar month
        valid_days = []

        if month_num in [1, 3, 5, 7, 8, 10, 12]:
            # 31 days in Jan, Mar, May, Jul, Aug, Oct, Dec
            valid_days = range(1, 32)
        elif month_num in [4, 6, 9, 11]:
            # 30 days in Apr, Jun, Sep, Nov
            valid_days = range(1, 31)
        elif month_num == 2 and Interface.is_leap_year(year_num):
            # 29 days in Feb for leap year
            valid_days = range(1, 30)
        elif month_num == 2 and not Interface.is_leap_year(year_num):
            # 28 days in Feb for non-leap year
            valid_days = range(1, 29)

        return day_num in valid_days

    @staticmethod
    def ph_num_check(ph_num):
        """
        Validate the length of a phone number.

        Args:
            ph_num (str): The phone number to validate.

        Returns:
            str: The phone number if valid.
        """

        if len(ph_num) > 10 or len(ph_num) < 9:
            print("Invalid phone number value!")
        else:
            return ph_num

    @staticmethod
    def email_check(email):
        """
        Validate the format of an email address.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        # Define a regular expression pattern for a valid email
        # This pattern allows for a wide range of valid email formats
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Use re.match to check if the email matches the pattern
        if re.match(email_pattern, email):
            return True
        else:
            return False

    @staticmethod
    def grade_check(grade):
        """
        Validate the input grade of a young learner's user.

        Args:
            grade (str): The grade input to validate.

        Returns:
            int: The grade if valid.
        """

        try:
            grade = int(grade)  # Convert the input to an integer
            if grade <= 0 or grade > 12:
                print("Invalid grade input!")
            else:
                return grade
        except ValueError:
            print("Please enter a valid integer!")
            print("Please enter values from 1 to 12.")

    # ===================================== Menus ===================================== #

    def main_menu(self):
        """
        Display the main menu options.

        Returns:
            None
        """

        print("\n---------- Welcome to CodeVenture ---------")

        print("\nPick your options:")
        print("\t1. Login")
        print("\t2. Register new account")
        print("\t3. Forgot password")
        print()

        while True:
            user_input = input("Enter 'q' to quit the program.\n"
                               "Please enter a menu option: ")

            try:
                user_input = int(user_input)
            except:
                if user_input == "q":
                    print("Thank you for playing!")
                    print("Hope to see you again.")
                    return
                print("Please enter a valid integer.")

            if user_input in range(1, 3 + 1):
                if user_input == 1:
                    print("\n.....Entering login menu.....")
                    self.login_menu()
                    # print("Exiting login menu...")
                    break
                elif user_input == 2:
                    print("\n.....Entering registration menu.....")
                    self.registration_menu()
                    # print("Exiting registration menu...")
                    break
                elif user_input == 3:
                    print("\n.....Entering reset password menu.....\n")
                    self.reset_password_menu()
                    # print("Exiting reset password menu...")
                    break
            else:
                print("Please enter a valid integer from 1-3.")

    def login_menu(self):
        """
        Allow users to log into their accounts.

        Returns:
            None
        """
        while True:
            username = input("\nPlease enter your username: ")
            if username == "q":
                return self.main_menu()
                break

            password = input("Please enter your password: ")
            if password == "q":
                return self.main_menu()
                break

            if User.authenticate(self.users_dict, username, password):
                self.current_user = username
                if isinstance(self.users_dict[self.current_user], Admin):
                    print()
                    print("--------- Successfully logged in as admin ---------\n")
                    return self.admin_interface()
                else:
                    print()
                    print ("-------- Successfully logged in as a young learner --------\n")
                    return self.learners_interface()
            else:
                print("Login attempt was unsuccessful")
                continue

    def registration_menu(self):
        """
        Allow users to create a new account.

        Returns:
            None
        """
        # Register the user
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")

        while True:
            try:
                year = int(input("Please enter your year of birth: "))
                month = int(input("Please enter your month of birth: "))
                day = int(input("Please enter your day of birth: "))

                if Interface.date_value_check(year, month, day):
                    dob = date(year, month, day)
                    break
                else:
                    print("Not a valid input! Please try again!")

            except:
                print("Invalid format!")

        # First check whether the username is unique or not
        while True:
            username = input("Please enter a username: ")
            if username in self.users_dict:
                print("Username is already taken!")
                continue
            else:
                break

        password = input("Please enter a password: ")

        while True:
            email = input("Please enter your email: ")
            if Interface.email_check(email):
                break
            print("Please enter your email again!")

        while True:
            ph_num = input("Please enter your phone number (without any symbols): ")
            if Interface.ph_num_check(ph_num):
                break
            print("Please enter your phone number again!")

        while True:
            grade = input("What Grade are you in?\n"
                          "Enter a number from 1 to 12: ")
            result = Interface.grade_check(grade)
            if result is not None:
                break

        YoungLearner.register(self.users_dict, first_name, last_name, username, password, dob, email, ph_num, grade)
        self.main_menu()

    def reset_password_menu(self):
        """
        Allow users to reset their password.

        Returns:
            None
        """
        while True:
            username = input("Please enter your username: ")
            if username in self.users_dict:
                new_password = input("Please enter your new password: ")
                confirmed_password = input("Please enter your new password again to confirm: ")
                if new_password == confirmed_password:
                    self.users_dict[username].set_password(new_password)
                else:
                    print("Both inputs does not match.")
                    continue
                print("\n......Password has been changed.......")
                break
            else:
                print("The user does not exist.")
                continue
        self.main_menu()

    def admin_interface(self):
        """
        Display the menu options for admin users.

        Returns:
            None
        """
        print("You have the following menu options:")
        print("\t1. Get user details")
        print("\t2. Get admin details")
        print("\t3. Log out")
        print("\t4. Shut down system")
        print()

        while True:
            try:
                user_input = int(input("Please enter a menu option: "))
                if user_input in range(1, 4 + 1):
                    if user_input == 1:
                        # View other user profile
                        u_username = input("Please enter the username of the user that you want to view: ")
                        user_str = self.users_dict[u_username].get_details()

                        print(f"\n------ {u_username}'s details ------\n")
                        print(user_str)
                        print("------------- End of details -------------\n")

                        self.admin_interface()
                        break

                    elif user_input == 2:
                        # View own admin profile
                        admin_str = self.users_dict[self.current_user].get_details()

                        print("\n------ Admin details -------\n")
                        print(admin_str)
                        print("------ End of details ------\n")

                        self.admin_interface()
                        break

                    elif user_input == 3:
                        # Log out
                        print("\n......Logging out......")
                        self.main_menu()
                        break

                    elif user_input == 4:
                        # Shut down
                        if isinstance(self.users_dict[self.current_user], Admin):
                            admin_password = input("Please enter your admin password: ")
                            if admin_password == "q":
                                # Abort shutdown attempt
                                continue
                            elif User.authenticate(self.users_dict, self.current_user, admin_password):
                                print("\n......Shutting down game......")
                                break
                            else:
                                print("Incorrect admin password.")
                    else:
                        print("You have not entered a valid menu option!",
                              "Please try again.")
            except Exception as e:
                print("Error:", e)
                print("Invalid input, please enter an integer.")

    def learners_interface(self):
        """
        Display the menu options for young learner users.

        Returns:
            None
        """

        print("\nYou have the following options:")
        print("\t1. View profile")
        print("\t2. Play game")
        print("\t3. Quizzes")
        print("\t4. Log out")
        print()

        while True:
            try:
                user_input = input("Please enter a menu option: ")
                if user_input == "1":
                    # View profile
                    user_details = YoungLearner.get_details(self.users_dict[self.current_user])
                    print()
                    print("-----------User Details------------\n")
                    print(user_details)
                    print("-----------------------------------\n")
                    self.learners_interface()
                    break

                elif user_input == "2":
                    new_game1 = Game("Class",
                                     ["What is a class?", "Instance Variables", "Instantiation"])  # sample data
                    try:
                        while new_game1.choose_game_difficulty() != "q":
                            new_game1.choose_lm()
                            new_game1.play_game()
                            self.learners_interface()
                    except:
                        self.learners_interface()

                elif user_input == "3":
                    # Display quizzes
                    try:
                        while Quizzes.start_quiz() != "q":
                            self.learners_interface()
                    except:
                        self.learners_interface()
                    # break

                elif user_input == "4":
                    # Log out
                    print("\n......Logging out......")
                    self.main_menu()
                    break

            except Exception as e:
                print("Error:", e)
                print("Invalid input, please enter an integer.")