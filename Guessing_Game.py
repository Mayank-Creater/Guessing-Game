import random
chance = 100
r = random.randint(1,100)
while chance > 0:
			n = int(input("Enter your guess"))
			if n > r:
				print("Guess is high")
				chance -= 1
			elif n < r:
				print("Guess is low")
				chance -= 1
			else:
				 print ("You guessed it right")
				 break
