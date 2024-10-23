import random

magic_number = random.randint(1,10)
print("Welcome to the Million dollar game, you will have multiples tries, think carefully")


while True:
  user_number=int(input("Guess the number between 1,10:"))
  
  if magic_number == user_number:
    print("You win!")
    break
  else:
    print("You lost!")
