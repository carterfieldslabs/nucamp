import random
import time

while True:
    if exit == True:
        break

    wizard = "Wizard"
    wizard_hp = 70
    wizard_damage = 150

    elf = "Elf"
    elf_hp = 100
    elf_damage = 100

    human = "Human"
    human_hp = 150
    human_damage = 20

    orc = "Orc"
    orc_hp = 250
    orc_damage = 120

    dragon_hp = 300
    dragon_damage = 50

    while True:
        print("1)   Wizard")
        print("2)   Elf")
        print("3)   Human")
        print("4)   Orc")
        print("5)   Exit")

        choice = input("Choose your character: ").lower()

        if choice == "1" or choice == wizard.lower():
            character = wizard
            my_damage = wizard_damage
            my_hp = wizard_hp
            break
        if choice == "2" or choice == elf.lower():
            character = elf
            my_damage = elf_damage
            my_hp = elf_hp
            break
        if choice == "3" or choice == human.lower():
            character = human
            my_damage = human_damage
            my_hp = human_hp
            break
        if choice == "4" or choice == orc.lower():
            character = orc
            my_damage = orc_damage
            my_hp = orc_hp
            break
        if choice == "5" or choice == exit.lower():
            exit = True
            break

        print("Invalid Selection")

    if exit != True:
        print("")
        print("You have chosen the character:", character)
        print("Health:", my_hp)
        print("Damage:", "1 -",my_damage)
        print("")
        char_name = input("What Name would you like to give your " + character + "? : ")
        print("")


    while True:
        if exit == True:
            break
        round_damage = random.randint(0, my_damage)
        dragon_hp = dragon_hp - round_damage
        if round_damage == 0:
            print(char_name, "the", character, "misses the Dragon!")
            print("The Dragon's hitpoints are now:", dragon_hp)
            print("")
            time.sleep(2)

        else:
            print(char_name, "the", character, "damaged the Dragon for", round_damage,"points!")
            print("The Dragon's hitpoints are now:", dragon_hp)
            print("")
            time.sleep(2)
        if dragon_hp <= 0:
            print(char_name, "the", character, "has slain The Dragon!")
            break
        
        dragon_round_dmg = random.randint(0, dragon_damage)
        my_hp = my_hp - dragon_round_dmg
        if dragon_round_dmg == 0:
            print("The Dragon misses the", char_name, "the", character)
            print(char_name, "the", character + "'s hitpoints are now:", my_hp)
            print("")
            time.sleep(2)
        else:
            print("The Dragon strikes back at", char_name, "the", character, "and hits for", dragon_round_dmg,"points!")
            print(char_name, "the", character + "'s hitpoints are now:", my_hp)
            print("")
            
        if my_hp <= 0:
            print(char_name, "the", character, "has lost the battle.")
            print("")
            break
        else:
            time.sleep(2)

    if exit == True:
        break

    play_again = input("Would you like to play again (Y/N): ").lower()
    if play_again != "y":
        print("")
        print("Thank you for playing!")
        print("")
        break