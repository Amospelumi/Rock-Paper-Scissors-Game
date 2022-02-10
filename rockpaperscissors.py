#  variables to print out result of each players.
result1 = "Rock smashes scissors"
result2 = "Paper covers rock"
result3 = "Scissors cut paper"


#  The main game function.
def Game():
    while 0 < 1:
        Player1 = input("Player1: Rock, Paper, Scissors? ").upper()
        Player2 = input("Player2: Rock, Paper, Scissors? ").upper()
        if Player1 == "ROCK" and Player2 == "SCISSORS":
            print(result1)
            break
        elif Player2 == "ROCK" and Player1 == "SCISSORS":
            print(result1)
            break
        elif Player1 == "PAPER" and Player2 == "ROCK":
            print(result2)
            break
        elif Player2 == "PAPER" and Player1 == "ROCK":
            print(result2)
            break
        elif Player2 == "SCISSORS" and Player1 == "PAPER":
            print(result3)
            break
        elif Player1 == "SCISSORS" and Player2 == "PAPER":
            print(result3)
            break
        elif Player1 == Player2:
            print("Sorry!, you both choose samething, Game continue.")
            continue
        else:
            print("Wrong input")
            break


Game()
