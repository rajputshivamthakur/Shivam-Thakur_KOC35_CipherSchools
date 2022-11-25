from random import randint
Cnumber = randint(1, 100)
print("Try to guess the number (between 1 and 100) in three guesses!\n")
score = 0



guess1 = int(input("Enter Your 1st Guess:---\n"))
while True:
    if guess1 < Cnumber:
        print("Your guess was too  small, have one more try.")
        break

    elif guess1 > Cnumber:
        print("Your guess was too high, have one more try.")
        break

    else:
        print("Congrat's! Great job!")
        score = score + 1
        break



guess2 = int(input("Enter Your 2nd Guess:---\n"))

while True:
    if guess2 < Cnumber:
        print("Your guess was too  small, have one more try.")
        break

    elif guess2 > Cnumber:
        print("Your guess was too high, have one more try.")
        break

    else:
        print("Congrat's! Great job!")
        score = score + 1
        break



guess3 = int(input("Enter Your 3rd Guess:---\n"))

while True:
    if guess3 < Cnumber:
        print("Better Luck Next Time!")
        break

    elif guess3 > Cnumber:
        print("Better Luck Next Time!")
        break

    else:
        print("Congrat's! Great job!")
        score = score + 1
        break

print("Your score is",score)