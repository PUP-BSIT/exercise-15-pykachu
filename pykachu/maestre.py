import os

class Maestre:
    CHOICE_SHOW_GREET = 1
    CHOICE_SHOW_INFO = 2
    CHOICE_SHOW_GOALS = 3
    CHOICE_SHOW_HOBBIES = 4
    CHOICE_SHOW_QUOTE = 5
    CHOICE_RETURN_TO_MAINMENU = 6

    def __init__(self):
        self.name = "Michael Rua S. Maestre"
        self.age = 20
        self.program = "BSIT 2-1"
        self.university = "PUP Taguig"

    def show_greet(self, message="\nHi there! Welcome to my profile!"):
        os.system('cls')
        print(message)
        print(f"My name is {self.name}.")
        input("\nPress Enter to continue...")

    def show_info(self):
        os.system('cls')
        print(f"My age is {self.age}.")
        print(f"My course is {self.program}.")
        print(f"I am studying at {self.university}.")
        print("I live in Upper Bicutan, Taguig City.")
        input("\nPress Enter to continue...")
    
    def show_goals(self):
        os.system('cls')
        print("One of my goals is to become stable in life, where I am happy "
              "and content with what I have.")
        input("\nPress Enter to continue...")
    
    def show_hobbies(self):
        os.system('cls')
        print("My hobby is preaching, playing badminton, and watching " 
              "competitive shows.")
        input("\nPress Enter to continue...")
        
    def show_quote(self):
        os.system('cls')
        print("\nMy favorite quote is from the Bible, Psalm 16:8 - " 
             "I keep Jehovah before me constantly. " 
             "Because he is at my right hand, "
             "I will never be shaken.")
        input("\nPress Enter to continue...")

    def display_menu(self):
        os.system('cls')
        print(f"\nMenu for {self.name}: ")
        print("1. Greetings")
        print("2. Basic Information")
        print("3. Goals")
        print("4. Hobbies")
        print("5. Favorite Quote")
        print("6. Return to Main Menu")
        
    def menu(self):
         # Display menu until user chooses to exit
        while True:
            self.display_menu()

            try:
                choice = int(input("Please select an option (1-6): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
                input("\nPress Enter to continue...")
                continue

            match choice:
                case self.CHOICE_SHOW_GREET:
                    self.show_greet()
                case self.CHOICE_SHOW_INFO:
                    self.show_info()
                case self.CHOICE_SHOW_GOALS:
                    self.show_goals()
                case self.CHOICE_SHOW_HOBBIES:
                    self.show_hobbies()
                case self.CHOICE_SHOW_QUOTE:
                    self.show_quote()
                case self.CHOICE_RETURN_TO_MAINMENU: # Return to Main Menu
                    print("Returning to the main menu...")
                    break
                case _:
                    print("Invalid choice. Please try again.")
                    input("\nPress Enter to continue...")