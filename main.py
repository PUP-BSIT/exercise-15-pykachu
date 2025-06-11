import os 
import platform

from pykachu.besa import Besa
from pykachu.bualat import bualat
from pykachu.serquina import Serquina
from pykachua.salespara import Salespara

besa = Besa()
serquina = Serquina()
salespara = Salespara()

class Choices:
    BESA_MODULE = 1
    BUALAT_MODULE = 2
    MAESTRE_MODULE = 3
    SALESPARA_MODULE = 4
    SERQUINA_MODULE = 5
    EXIT = 6

def clear_screen():
    # Clear the console screen based on the operating system.
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def buffer_input():
    # Wait for user input to continue.
    input("\nPress 'Enter' to continue...")

def main():
    # Display menu until user chooses to exit
    while True:
        clear_screen()
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
            buffer_input()
            continue

        match user_choice:
            case Choices.BESA_MODULE:
                clear_screen()
                besa.run_menu()
            case Choices.BUALAT_MODULE:
                clear_screen()
                bualat.menu()
            case Choices.MAESTRE_MODULE:
                clear_screen()
                # TODO: Implement Maestre module functionality
            case Choices.SALESPARA_MODULE:
                clear_screen()
                salespara.run_menu()
            case Choices.SERQUINA_MODULE:
                clear_screen()
                serquina.run_menu()
            case 6:
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option (1-6).")

        buffer_input()

main()