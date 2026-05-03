import random

dice1output = random.randint(1, 6)
dice2output = random.randint(1, 6)
yes = "y"
no = "n"

while True:
    command = input('Roll the dice y/n: ')

    if command == yes:
        print(dice1output, dice2output)

    elif command == no:
        print("Thanks for playing!")
        break

    else:
        print("Invalid response, input y or n")