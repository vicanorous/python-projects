import random

inputchoices = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissor"
}

userinput = input("Choose: Rock, Paper, or Scissor (r/p/s): ").lower()
choices = ("r", "p", "s")
computerinput = random.choice(choices)


print(userinput)
if userinput not in (choices):
    print("Invalid response, input 'r', or 'p', or 's'")
    
else:
    print("You chose: " + userinput)
    print("Computer chose: " + computerinput)

if userinput == computerinput:
    print("It's a tie")
elif (userinput == "r" and computerinput == "s") or (userinput == "p" and computerinput == "r") or (userinput == "s" and computerinput == "p"):
    print("You win")

else:
    print("You lose")
