import random

magic_number = random.randint(1,10)

print ("Welcome To The Game That Will Make You Win, A Million Of Dollar, If You Guessing Correct It")
user_number=int(input("Guess the number between 1,10: "))



if magic_number == user_number:
  print("You win!")
else:
  print("You lost!")

