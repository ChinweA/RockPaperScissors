import random
import os

possible_options = ["R", "P", "S"] #"R" for Rock, "P" for Paper, "S" for Scissors
dict_options = {"R": "Rock", "P": "Paper", "S": "Scissors"}

print('"R" for "rock",\n"P" for "paper",\n"S" for "scissors"')
while True:
    user = input('Pick an option between "R", "P" or "S" \n') #User's guess
    CPU = random.choice(possible_options)  # Computer's guess
    if user not in possible_options:
        print('Input not valid. Try again.')
    else:
        if user == "R" and CPU == "P" or user == "P" and CPU == "R":
            # Paper covers Rock
            print(f'Player ({dict_options[user]}) : CPU ({dict_options[CPU]})')git push --set-upstream origin master
            winner = "Computer" if CPU == "P" else "Player"
            print(f"{winner} Wins!")

        if user == "R" and CPU == "S" or user == "S" and CPU == "R":
            # Rock crushes Scissors
            print(f'Player ({dict_options[user]}) : CPU ({dict_options[CPU]})')
            winner = "Computer" if CPU == "R" else "Player"
            print(f"{winner} Wins!")

        if user == "P" and CPU == "S" or user == "S" and CPU == "P":
            # Scissors cuts Paper
            print(f'Player ({dict_options[user]}) : CPU ({dict_options[CPU]})')
            winner = "Computer" if CPU == "S" else "Player"
            print(f"{winner} Wins!")

        if user == CPU:
            os.system("python RPS.py")
