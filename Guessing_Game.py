import random

random_number= random.randint(1,10) # number 1 - 10

guess = input("Pikc a number from 1 to 10:  ")
guess = int(guess)


while guess != random_number
    guess = input("Pick a number from 1 to 10:  ")
    guess = int(guess)
    
    if guess < random_number:
        print("TOO LOW")
    elif guess > random_number:
        

if guess == random_number:
    print("YOU GOT IT")
elif guess < random_number:
    print("TOO LOW!")
else:
    print("TOO HIGHT!")

print(random_number)
