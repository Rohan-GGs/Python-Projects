import random
print("Hey welcome to the number gussing game. Before getting started choose the diffulty you are comfortable with!!")
print("E = Easy , N = Normal, H = Hard")

def game(): 
    random_num = random.randint(1,100)
    b = input("Choose the difficulty(E/N/H):") 
    if b.upper() == "E":
        a = 14
    elif b.upper() == "N":
        a = 9
    else: 
        a = 4
        
    while a >= 0:
        
        guess_num = int(input("Guess the number from 1 to 100 : "))
        
        if guess_num > random_num:
            print("The random number is lower")
            print(f"You have {a} tries remaining")
        
        elif guess_num < random_num:
            print("The random number is higher")
            print(f"You have {a} tries remaining")
        else:
            print(f"You Won!!!, You guessed the right number which was {random_num}.")
            break
        a -= 1

    if a < 0:
        print("Sorry!, Better luck next time")
        print(f"The right number was {random_num}")

game()
z = 1
while z == 1:   
    c = input("Play again? (Y/N):")
    if c.upper() == "Y":
        game()
    else:
        print("Thank you!!")
        break
        