userinput = input("Choose: Rock, Paper, or Scissor (r/p/s): ")
rock = "r"
paper = "p"
scissor = "s"

while True:
    print(userinput)
    if userinput != rock and userinput != scissor and userinput != paper:
        print("Invalid response, input 'r', or 'p', or 's'")
        break
        