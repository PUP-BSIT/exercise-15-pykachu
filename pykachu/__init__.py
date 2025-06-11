class Serquina:
    CHOICE_GREET = 1
    CHOICE_INFO = 2
    CHOICE_MOTTOS = 3
    CHOICE_GOALS = 4
    CHOICE_EXIT = 5

    def __init__(self, name, age, program, university):
        self.name = name
        self.age = age
        self.program = program
        self.university = university

    def greet(self, message="Good day!"):
        print(message)
        print(f"My name is {self.name}.")

    def personal_info(self):
        print("\nPersonal Information:")
        print(f"I am {self.age} years old.")
        print(f"I am pursuing {self.program} program.")
        print(f"I am currently studying at {self.university}.")
        print("I live in Central Signal, Taguig City.")

    def my_mottos(self):
        print("\nMy Mottos:")
        print("1. A life ain't a life till you live it.")
        print("2. Everything happens for a reason.")
        print("3. You can't control the wind, but you can adjust your sails.")

    def my_goals(self):
        print("\nMy Goals in Life:")
        print("1. My goal is to be a successful UI Designer.")
        print("2. I want to go to Japan and drink matcha tea.")
        print("3. I hope to repay my parents for all their sacrifices.")

    def display_menu(self):
        print("\n1. Greetings")
        print("2. Personal Information")
        print("3. Mottos")
        print("4. Goals in Life")
        print("5. Exit")
        return int(input("Please enter your choice: "))

    def menu(self):
        choice = self.display_menu()
        while choice != self.CHOICE_EXIT:
            match choice:
                case self.CHOICE_GREET:
                    self.greet()
                case self.CHOICE_INFO:
                    self.personal_info()
                case self.CHOICE_MOTTOS:
                    self.my_mottos()
                case self.CHOICE_GOALS:
                    self.my_goals()
                case _:
                    print("\nInvalid choice! Please try again.")
            choice = self.display_menu()
        print("Exiting the menu.")

zcintilla = Serquina("Zcintilla R. Serquina", 20, "BSIT", "PUP - Taguig")
zcintilla.menu()