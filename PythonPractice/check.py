from random import randint

Game=randint(1, 100)

turn=0
while turn <5:
    guess_number=int(input("Enter your lucky number: "))
    turn+=1

    if Game > guess_number:
        if Game - guess_number <= 10:
            print("Your number is near (small)")
        else:
            print("your are too small")

    elif Game < guess_number:
        if guess_number - Game <= 10:
            print("Your number is near (big)")
        else:
            print("your number too big")

    elif Game == guess_number:
        print("Congratulations, YOU WIN")
        break
if turn==5:
    print("you are out of turn")