                ###   Mario Project

import random

class Character():
    def __init__(self, name):
        self.name = name
        self.__life = 3
        self.__score = 0

    def kicked(self):
        self.__score += 10

    def punched(self):
        self.__score += 5

    def stabbed(self):
        self.__life -= 1

    def display_life(self):
        return self.__life

    def display_score(self):
        return self.__score

    def __str__(self):
        return f"name={self.name}\nlife={self.__life}\nscore={self.__score}"

def main():
    name = input("Enter character's name: ")
    character = Character(name)

    while character.display_life() > 0:
        print("\nCharacter Actions:")
        print("1. Kick")
        print("2. Punch")
        print("3. Stab")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            character.kicked()
            print(f"{character.name} kicked and gained 10 points.")
        elif choice == "2":
            character.punched()
            print(f"{character.name} punched and gained 5 points.")
        elif choice == "3":
            character.stabbed()
            print(f"{character.name} was stabbed and lost 1 life.")
        elif choice == "4":
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please try again.")

        if character.display_life() == 0:
            print("Game over")
        else:
            print(f"{character.name} Status:")
            print(f"Life: {character.display_life()}")
            print(f"Score: {character.display_score()}")

if __name__ == "__main__":
    main()
