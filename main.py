import os 

from pykachu.bualat import bualat

class Choices:
    BESA_MODULE = 1
    BUALAT_MODULE = 2
    MAESTRE_MODULE = 3
    SALESPARA_MODULE = 4
    SERQUINA_MODULE = 5
    EXIT = 6

def main():
    # Display menu until user chooses to exit
    while True:
        os.system('cls')
        print("Welcome to the Group Package Program!")
        print("1. Besa Module")
        print("2. Bualat Module")
        print("3. Maestre Module")
        print("4. Salespara Module")
        print("5. Serquina Module")
        print("6. Exit")

        try:
            user_choice = int(input("\nSelect an option (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("\nPress Enter to continue...")
            continue

        match user_choice:
            case Choices.BESA_MODULE:
                os.system('cls')
                # TODO: Implement Besa module functionality
            case Choices.BUALAT_MODULE:
                os.system('cls')
                bualat.menu()
            case Choices.MAESTRE_MODULE:
                os.system('cls')
                # TODO: Implement Maestre module functionality
            case Choices.SALESPARA_MODULE:
                os.system('cls')
                # TODO: Implement Salespara module functionality
            case Choices.SERQUINA_MODULE:
                os.system('cls')
                # TODO: Implement Serquina module functionality
            case 6:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option (1-6).")

        input("\nPress Enter to continue...")

main()