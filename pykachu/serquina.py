import os

class Serquina:
    GREET_OPTION = 1
    AGE_OPTION = 2
    COURSE_OPTION = 3
    YEAR_OPTION = 4
    GOALS_OPTION = 5
    MAIN_MENU_OPTION = 6

    def __init__(self):
        self.name = "Zcintilla R. Serquina"
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

    def display_goals(self):
        goals = [
            "To be a successful UI Designer.",
            "To go to Japan and drink matcha tea.",
            "To repay my parents for all their sacrifices.",
        ]

        print("\nMy goals are:")
        for goal in goals:
            print(f"- {goal}")

    def buffer_input(self):
        input("\nPress [ENTER] to continue.")

    def clear_screen(self):
        os.system('cls')

    def menu(self):
        print("\n---[Serquina's Menu]---")
        print("--------------------")
        print(f"[{self.GREET_OPTION}] - Greet")
        print(f"[{self.AGE_OPTION}] - Display Age")
        print(f"[{self.COURSE_OPTION}] - Display Course")
        print(f"[{self.YEAR_OPTION}] - Display Year")
        print(f"[{self.GOALS_OPTION}] - Display Goals")
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

    def handle_goals_option(self):
        self.display_goals()
        self.buffer_input()

    def run_menu(self):
        # Loop until the user selects 'Return to Main Menu'
        while True:
            self.clear_screen()
            self.menu()

            try:
                user_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number "
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
                    case self.GOALS_OPTION:
                        self.handle_goals_option()
                    case self.MAIN_MENU_OPTION:
                        break
                    case _:
                        print("Invalid option. Please try again.")
                        self.buffer_input()