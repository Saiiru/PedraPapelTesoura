print("made by Sairu")
import time
loose = ("The computer wins")
win = ("You Win")
lives = 5
score = 0
drew = 0
computer_lives = 7
password_list = []
while True:
    print("To begin fill in the below information.")
    username = input("Please enter your username:  ")
    password = input("Please enter your password:  ")
    searchfile = open("accounts.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
                print("Access Granted")
                time.sleep(0.5)
                print("Loading.")
                time.sleep(0.5)
                print("Loading..")
                time.sleep(0.5)
                print("Loading...")
                time.sleep(0.5)
                start_menu = """
                ROCK PAPER SCISSORS LIZARD SPOCK
                """

                print(start_menu)
                while True:
                    rps = input("Rock, Paper, Scissors, Lizard, Spock?   ")
                    rps = rps.title()
                    import random
                    computer = ("rock", "paper", "scissors", "lizard", "spock")
                    computer = random.choice(computer)
                    #rock if statments
                    if rps == "Rock" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    if rps == "Rock" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        print("")
                        print("")
                        score+=1
                    if rps == "Rock" and computer == "lizard":
                        print("the computer choose",computer)
                        print("")
                        print("loose")
                        print("")
                        print("")
                        score-=1
                    if rps == "Rock" and computer == "lizard":
                        print("the computer choose",computer)
                        print("")
                        print("win")
                        print("")
                        print("")
                        score += 1
                  #paper if statements
                    if rps == "Paper" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score += 1
                    if rps == "Paper" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives -= 1
                    if rps == "Paper" and computer == "lizard":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score += 1
                    if rps == "Paper" and computer == "spock":
                        print("The computer choose", computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives -= 1
                    #scissor if statements
                    if rps == "Scissors" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score+=1
                    if rps == "Scissors" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    if rps == "Scissors" and computer == "spock":
                        print("The computer choose",computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score+=1
                    if rps == "Scissors" and computer == "lizard":
                        print("The computer choose",computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives-=1
                    #Lizard if statements
                    if rps == "Lizard" and computer == "paper":
                        print("The computer choose", computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score += 1
                    if rps == "Lizard" and computer == "rock":
                        print("The computer choose", computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives -= 1
                    if rps == "Lizard" and computer == "spock":
                        print("The computer choose", computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score += 1
                    if rps == "Lizard" and computer == "scissors":
                        print("The computer choose", computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives -= 1
                    # spock if statements
                    if rps == "Spock" and computer == "rock":
                        print("The computer choose", computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score += 1
                    if rps == "Spock" and computer == "paper":
                        print("The computer choose", computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives -= 1
                    if rps == "Spock" and computer == "scissors":
                        print("The computer choose", computer)
                        print("")
                        print(win)
                        computer_lives -= 1
                        print("")
                        print("")
                        score += 1
                    if rps == "Spock" and computer == "lizard":
                        print("The computer choose", computer)
                        print("")
                        print(loose)
                        print("")
                        print("")
                        lives -= 1
                    #duplicates
                    if rps == "Rock" and computer == "rock":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1               
                    if rps == "Paper" and computer == "paper":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                    if rps == "Scissors" and computer == "scissors":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                    if rps == "Lizard" and computer == "lizard":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1
                    if rps == "Spock" and computer == "spock":
                        print("The computer choose",computer)
                        print("")
                        print("You Drew")
                        print("")
                        print("")
                        drew+=1

                    #system
                    if rps == "rules":
                        print("**********************************************")
                        print("Rules")
                        print("**********************************************")
                        print("-Paper covers Rock ")
                        print("-Spock smashes Scissors ")
                        print("-Scissors cuts Paper ")
                        print("-Rock crushes Lizard ")
                        print("-Lizard poisons Spock ")
                        print("-Scissors decapitates Lizard ")
                        print("-Lizard eats Paper ")
                        print("-Paper disproves Spock ")
                        print("-Spock vaporizes Rock ")
                        print("-Rock crushes Scissors ")
                        print("**********************************************")
                    if rps == "display lives":
                        print(lives)
                    if rps == "display score":
                        print(score)
                    if rps == "display drew":
                        print(drew)
                    #lives
                    if lives == 0 or rps == "test":
                        print("Thanks for playing.")
                        print("You have run out of lives")
                        print("You got",score,"correct")
                        print("You drew",drew,"times")
                        stop = input("Press enter to exit.")
                        exit()
                    if computer_lives == 0:
                        print("Thanks for playing.")
                        print("The computer lost all it's lives. You Win.")
                        print("You got",score,"correct")
                        print("You drew",drew,"times")
                        stop = input("Press enter to exit.")
                        exit()
                    #exit
                    if rps == "exit":
                        break
        if password in line and password != line:
            print("Your username or password is incorrect.")
            print("---------------------------------------")
