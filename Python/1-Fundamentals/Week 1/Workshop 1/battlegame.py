wizard_hp = 70
wizard_damage = 150

elf_hp = 100
elf_damage = 100

human_hp = 150
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print("List of characters are: Wizard, Elf, Human")
    print("1) Wizard \n2) Elf \n3) Human")
    print("Choose your character")
    x = int(input())
    if x == 1:
        character = "Wizard"
        print("You have chosen the character: ", character)
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif x == 2:
        character = "Elf"
        print("You have chosen the character: ", character)
        my_hp = elf_hp
        my_damage = elf_damage
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    elif x == 3:
        character = "Human"
        print("You have chosen the character: ", character)
        my_hp = human_hp
        my_damage = human_damage
        print("Health: ", my_hp)
        print("Damage: ", my_damage)
        break
    else:
        print("Unknown Character")
