import random



def Rules():
	print("The game will begin with you either choosing to be the guesser or the one \
	generating the number.  The person generating the number will choose a 3 digit number with no \
	repeated digits.  The person guessing will then attempt to guess that 3 digit number.  If \
	the guess has no correct numbers, the person who made the number will say bagel, if it has a \
	correct digit but in the wrong spot they will say Pico, and a correct digit in the right spot \
	they will say Fermi.  Always say any Picos before Firmis.  The guesser will keep attempting to \
	guess numbers until a correct number is found. TEST")

def startGame():
	gamemode = 0
	while gamemode != "guessing" and gamemode != "creating":
		gamemode = input("Would you like to be the player guessing the number or creating the number? \
			please input 'guessing' or 'creating'\n " )
	return gamemode

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
	playerGuess = [] #guess starts empty
	digits = ["0","1","2","3","4","5","6","7","8","9"] #list of digits so we can make sure guess is a number
	while playerGuess != numtoGuess:
		playerGuess = [0,0,0]
		print(numtoGuess)
		response = [] #starts blank until guess is made

		#ensure that guess has no repeated digit
		while playerGuess[0] in playerGuess[1:] or playerGuess[1] == playerGuess[2]:	
			guessString = input("Guess a 3 digit number with no spaces in between numbers and no repeats: ")
			
			#check for characters other than number in guess
			while guessString[0] not in digits \
			or guessString[1] not in digits or guessString[2] not in digits:
				print("please make a guess using only the numbers 0-9")
				guessString = input("Guess a 3 digit number with no spaces in between numbers and no repeats: ")
			
			#makes sure guess is 3 digits long
			while len(guessString) != 3:
				print("please make a guess only 3 digits in length")
				guessString = input("Guess a 3 digit number with no spaces in between numbers and no repeats: ")
			
			temp = []
			
			for ch in guessString:
				temp.append(int(ch)) #makes a list with guess
			
			for i in range(len(temp)):
				playerGuess[i] = temp[i] #makes player guess = to new guess



		if playerGuess[0] not in numtoGuess: #this code is for bagels
			if playerGuess[1] not in numtoGuess and playerGuess[2] not in numtoGuess:
				response.append("Bagel")
			else: 
					pass
		

		#code for Pico / Fermi
		for ch in range(len(playerGuess)):
			if playerGuess[ch] in numtoGuess:
				if playerGuess[ch] == numtoGuess[ch]:
					response.insert(4, "Fermi") #inserted at 4 to ensure Fermis always come last
				else:
						response.insert(0, "Pico") #inserted at 0 to ensure Pico's come first
		print(response)
	print("Congradulations, you guessed the correct number!")

def creating():
	print("The computer will make a guess then you will input the correct response \
		if you input fermi fermi fermi, then the guess is correct and the game will be over")
	

def main():
	gamemode = startGame()
	if gamemode == "guessing":
		test = generateNum()
		guessing(test)
	if gamemode == "creating":
		creating()

if __name__ == "__main__":
	main()
