import random

def Rules():
	print("The game will begin with you either choosing to be the guesser or the one \
	generating the number.  The person generating the number will choose a 3 digit number with no \
	repeated digits.  The person guessing will then attempt to guess that 3 digit number.  If \
	the guess has no correct numbers, the person who made the number will say bagel, if it has a \
	correct digit but in the wrong spot they will say Pico, and a correct digit in the right spot \
	they will say Fermi.  Always say any Picos before Firmis.  The guesser will keep attempting to \
	guess numbers until a correct number is found.")

def startGame():
	gamemode = input("Would you like to be the player guessing the number or creating the number? \
		please input 'guessing' or 'creating' " )

def generateNum():
	number1 = random.randint(1,9) 
	number2 = 90
	while number2 == 90:
		possible2 = random.randint(0,9)
		if possible2 != number1:
			number2 = possible2
	number3 = 90
	while number3 == 90:
		possible3 = random.randint(0,9)
		if possible3 != number1 and possible3 != number2:
			number3 = possible3
	numtoGuess = [number1, number2, number3]
	return numtoGuess

def guessing(numtoGuess):
	playerGuess = []
	while playerGuess != numtoGuess:
		playerGuess = []
		response = []
		print(numtoGuess)
		guessString = input("Guess a 3 digit number: ")
		for ch in guessString:
			playerGuess.append(int(ch))

		if playerGuess[0] not in numtoGuess: #this code is for bagels
			if playerGuess[1] not in numtoGuess and playerGuess[2] not in numtoGuess:
				response.append("Bagel")
			else: 
					pass
		else: 
			pass

		#code for Pico
		for ch in range(len(playerGuess)):
			if playerGuess[ch] in numtoGuess:
				if playerGuess[ch] == numtoGuess[ch]:
					response.insert(4, "Fermi")
				else:
						response.insert(0, "Pico")
		print(response)






def main():
	# if gamemode == "guessing":
	# 	guessing()
	test = generateNum()
	guessing(test)

if __name__ == "__main__":
	main()