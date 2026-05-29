import random

chosen_num = random.randint(19, 79)
input_num = 0

while input_num != chosen_num:
    input_num = int(input("Guess the chosen number: "))

    if input_num < chosen_num:
        print(f"{input_num} is incorrect, guess higher")

    elif input_num > chosen_num:
        print(f"{input_num} is incorect, guess lower")
    
    else:
        print(f"{input_num} is the chosen number")
    