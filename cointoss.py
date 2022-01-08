import random


print("Welcome to coin toss!")
print("**************************************")
print("Instructions: Choose either 'heads' or 'tails' and if you guess correctly then you get points best out of 5")

def cointoss():
  
  count = 0

  for i in range(5):
    ans = random.randint(0,1)
    guess = input("Enter a guess: ")

    if ans == 0: 
      print("You have gotten heads")

    if ans == 1: 
      print("You have gotten tails")

    if guess == "heads" and ans == 0:
      count += 1
    
    if guess == "tails" and ans == 1:
      count += 1

  if count != 5:
    return f"Correct number of guesses is {count},your score is: {(count/5) * 100}%"
  else:
    return "Great Job you got all 5 guesses correct and scored 100% :)"

print(cointoss())
