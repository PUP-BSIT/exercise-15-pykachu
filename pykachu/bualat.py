import os

class BualatInfo:
    CHOICE_SHOW_NAME = 1
    CHOICE_SHOW_OVERVIEW = 2
    CHOICE_SHOW_GOAL = 3
    CHOICE_SHOW_TRAITS = 4
    CHOICE_SHOW_CRUSH = 5
    CHOICE_EXIT = 6

    def __init__ (self, name, overview, goal, traits, crush):
        self.name = name
        self.overview = overview
        self.goal = goal
        self.traits = traits
        self.crush = crush

    def show_name(self):
        os.system('cls')
        print(f"Name: {self.name}")

    def show_overview(self):
        os.system('cls')
        print(f"Overview: {self.overview}")

    def show_goal(self):
        os.system('cls')
        print(f"Goal: {self.goal}")

    def show_traits(self):
        os.system('cls')
        print("Traits:")
        for trait in self.traits:
            print(f"- {trait}")

    def show_crush(self):
        os.system('cls')
        print(f"Crush: {self.crush}")

    def menu(self):
        # Display menu until user chooses to exit
        while True:
            os.system('cls')
            print(f"Menu for {self.name}:")
            print("1. Name")
            print("2. Overview")
            print("3. Goal")
            print("4. Traits")
            print("5. Crush")
            print("6. Return to main menu")

            try:
                user_choice = int(input("Please enter your choice (1-6): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
                input("\nPress Enter to continue...")
                continue
            
            match user_choice:
                case self.CHOICE_EXIT: # Return to main menu
                    print("\nReturning to main menu...")
                    break
                case self.CHOICE_SHOW_NAME:
                    self.show_name()
                    input("\nPress Enter to continue...")
                case self.CHOICE_SHOW_OVERVIEW:
                    self.show_overview()
                    input("\nPress Enter to continue...")
                case self.CHOICE_SHOW_GOAL:
                    self.show_goal()
                    input("\nPress Enter to continue...")
                case self.CHOICE_SHOW_TRAITS:
                    self.show_traits()
                    input("\nPress Enter to continue...")
                case self.CHOICE_SHOW_CRUSH:
                    self.show_crush()
                    input("\nPress Enter to continue...")
                case _:
                    print("Invalid choice. Please select a valid choice.")
                    input("\nPress Enter to continue...")

bualat = BualatInfo(
    name = "Bench Brian Bualat",
    overview = (
        "I like to play online games and watch movies. "
        "I don't have a girlfriend in my entire life. " 
        "But I have a family and friends who love and support me. " 
        "I am a simple person who enjoys the little things in life."
    ),
    goal = (
        "To be rich, but also to be happy and content with what I have."
        " Provide everything for my family and friends."
    ),
    traits = ["Cruel", "Chaotic", "Friendly", "Loyal", "Simple"],
    crush = "Nini <3"
)
