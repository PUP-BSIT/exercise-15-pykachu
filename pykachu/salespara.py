import os

class Salespara:
    GREET_OPTION = 1
    AGE_OPTION = 2
    PROGRAM_OPTION = 3
    YEAR_OPTION = 4
    TRAITS_OPTION = 5
    MAIN_MENU_OPTION = 6

    def __init__(self):
        self.name = "Rica Genevive B. Salespara"
        self.age = 20
        self.program = "Bachelor of Science in Information Technology"
        self.year = "2nd Year Level"

    def greet(self):
        print(f"\nHello! I am {self.name}.")

    def display_age(self):
        print(f"\nI am {self.age} years old.")

    def display_program(self):
        print(f"\nI am pursuing {self.program}.")

    def display_year(self):
        print(f"\nI am currently in my {self.year} at PUP-Taguig.")

    def display_traits(self):
        traits = [
            "Growth-oriented",
            "Sophisticated",
            "Soft-hearted",
            "Carefree",
            "Radiant",
        ]
        print("\n-------Salespara's Traits-------")
        for trait in traits:
            print(f"- {trait}")

    def buffer_input(self):
        input("\nPress [ENTER] to continue...")

    def clear_screen(self):
        os.system('cls')

    def menu(self):
        print("\n------[Salespara's Menu]------")
        print("-------------------------------")
        print(f"[{self.GREET_OPTION}] - Greetings")
        print(f"[{self.AGE_OPTION}] - Display Age")
        print(f"[{self.PROGRAM_OPTION}] - Display Program")
        print(f"[{self.YEAR_OPTION}] - Display Year Level")
        print(f"[{self.TRAITS_OPTION}] - Display Traits")
        print(f"[{self.MAIN_MENU_OPTION}] - Return to Main Menu")
        print("-------------------------------")
        
    def handle_greet_option(self):
        self.greet()
        self.buffer_input()

    def handle_age_option(self):
        self.display_age()
        self.buffer_input()

    def handle_program_option(self):
        self.display_program()
        self.buffer_input()

    def handle_year_option(self):
        self.display_year()
        self.buffer_input()

    def handle_traits_option(self):
        self.display_traits()
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
                    case self.PROGRAM_OPTION:
                        self.handle_program_option()
                    case self.YEAR_OPTION:
                        self.handle_year_option()
                    case self.TRAITS_OPTION:
                        self.handle_traits_option()
                    case self.MAIN_MENU_OPTION:
                        print("\nReturning to main menu...")
                        break
                    case _:
                        print("Invalid option. Please try again.")
                        self.buffer_input()