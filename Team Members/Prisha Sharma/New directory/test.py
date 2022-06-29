from random import randint

guess = int(input("Enter a 4 digit number: "))
random_num = randint(1000, 10000)

if guess > random_num:
    print("Too High")
else:
    print("Too Low")
if guess == random_num:
    print("Good Job")













