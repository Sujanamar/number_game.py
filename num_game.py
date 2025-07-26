import random

  secret_number = random.randomint(1,10)
  

  print("guess the number (between 1 and 10):")

  while True:
      guess=int(input("your guess:"))


      if guess==secret_number:
