import os
import platform

class Besa:
    GREET_OPTION = 1
    AGE_OPTION = 2
    COURSE_OPTION = 3
    YEAR_OPTION = 4
    HOBBIES_OPTION = 5
    MAIN_MENU_OPTION = 6

    def __init__(self):
        self.name = "Vince Adrian A. Besa"
        self.age = 20
        self.course = "Bachelor of Science in Information Technology"
        self.year = "2nd Year"

    def greet(self):
        print(f"\nHello, I am {self.name}.")

    def display_age(self):
        print(f"\nI am {self.age} years old.")

    def display_course(self):
        print(f"\nI am taking {self.course}.")

    def display_year(self):
        print(f"\nI am currently in my {self.year} at PUP-Taguig.")

    def display_hobbies(self):
        hobbies = [
            "Playing video games",
            "Watching classic movies",
            "Listening to music",
            "Singing",
            "Reading books",
            "Cooking",
            "Exploring new technologies",
        ]

        print("\nMy hobbies are:")
        for hobby in hobbies:
            print(f"- {hobby}")

    def buffer_input(self):
        input("\nPress 'Enter' to continue...")

    def clear_screen(self):
        # Clear screen based on OS
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def display_menu(self):
        print("\n---[Besa's Menu]---")
        print("--------------------")
        print(f"[{self.GREET_OPTION}] - Greet")
        print(f"[{self.AGE_OPTION}] - Display Age")
        print(f"[{self.COURSE_OPTION}] - Display Course")
        print(f"[{self.YEAR_OPTION}] - Display Year")
        print(f"[{self.HOBBIES_OPTION}] - Display Hobbies")
        print(f"[{self.MAIN_MENU_OPTION}] - Return to Main Menu")
        print("--------------------")

    def handle_greet_option(self):
        self.greet()
        self.buffer_input()

    def handle_age_option(self):
        self.display_age()
        self.buffer_input()

    def handle_course_option(self):
        self.display_course()
        self.buffer_input()

    def handle_year_option(self):
        self.display_year()
        self.buffer_input()

    def handle_hobbies_option(self):
        self.display_hobbies()
        self.buffer_input()

    def run_menu(self):
        # Loop until the user selects 'Return to Main Menu'
        while True:
            self.clear_screen()
            self.display_menu()

            try:
                user_choice = int(input("Please select an option: "))
            except ValueError:
                print("\nInvalid input. Please enter a number "
                      "corresponding to the menu options.")
                self.buffer_input()
                continue
            
            match user_choice:
                    case self.GREET_OPTION:
                        self.handle_greet_option()
                    case self.AGE_OPTION:
                        self.handle_age_option()
                    case self.COURSE_OPTION:
                        self.handle_course_option()
                    case self.YEAR_OPTION:
                        self.handle_year_option()
                    case self.HOBBIES_OPTION:
                        self.handle_hobbies_option()
                    case self.MAIN_MENU_OPTION:
                        pass
                    case _:
                        print("Invalid option. Please try again.")
                        self.buffer_input()