import random

chosen_num = random.randint(19, 79)
input_num = 0

while input_num != chosen_num:
    input_num = int(input("Guess the chosen number: "))

    if input_num < chosen_num:
        print(f"{input_num} is incorrect, guess lower")

    elif input_num > chosen_num:
        print(f"{input_num} is incorect, guess higher")
    
    else:
        print(f"{input_num} is incorrect, how dumb can you be bitch! GUESS HIGHER!!!")