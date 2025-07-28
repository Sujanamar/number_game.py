

import random;

  secret_number = random.randomint(1,100)
  

  print("guess the number (between 1 and 100):")

  while True:
      guess=int(input("your guess:"))


      if guess==secret_number:
          print("congratulations! you guessed it right!")
        

      break
  elif guess < secret_number:
      print("too high.try again.")

  else:
      print("too low.try again.")


