import random

stringdigits = ["0","1","2","3","4","5","6","7","8","9"] #list of digits 
digits = [0,1,2,3,4,5,6,7,8,9]
FermiIndex = 0

def Rules():
	print("The game will begin with you either choosing to be the guesser or the one \
generating the number.  The person generating the number will choose a 3 digit number with no \
repeated digits.  The person guessing will then attempt to guess that 3 digit number.  If \
the guess has no correct numbers, the person who made the number will say bagel. If it has a \
correct digit but in the wrong spot they will say Pico for each of those digits. If it has a correct digit\
in the right spot they will say Fermi for each digit.  Always say any Picos before Firmis.  The guesser will \
keep attempting to guess numbers until a correct number is found.\n")

def startGame():
	gamemode = 0
	while gamemode != "Guessing" and gamemode != "Creating":
		gamemode = input("Would you like to be the player guessing the number or creating the number? \
Please input 'Guessing' or 'Creating'\n " )
		print() #this print statement and all other following input statements are just to make it easier on the
				#eyes in terminal	

	return gamemode

def generateNum():
	number1 = digits[random.randint(1,len(digits)-1)] 
	number2 = 90
	while number2 == 90:
		possible2 = digits[random.randint(0,len(digits)-1)]
		if possible2 != number1:
			number2 = possible2
	number3 = 90
	while number3 == 90:
		possible3 = digits[random.randint(0,len(digits)-1)]
		if possible3 != number1 and possible3 != number2:
			number3 = possible3
	numtoGuess = [number1, number2, number3]
	digits.remove(number1)
	digits.remove(number2)
	digits.remove(number3)
	return numtoGuess

def guessing(numtoGuess):
	playerGuess = [] #guess starts empty
	while playerGuess != numtoGuess:
		playerGuess = [0,0,0]
		print(numtoGuess)
		response = [] #starts blank until guess is made

		#ensure that guess has no repeated digit
		while playerGuess[0] in playerGuess[1:] or playerGuess[1] == playerGuess[2]:	
			guessString = input("Guess a 3 digit number with no spaces in between numbers and no repeats: ")
			print()
			#check for characters other than number in guess
			while guessString[0] not in stringdigits \
			or guessString[1] not in stringdigits or guessString[2] not in stringdigits:
				print("please make a guess using only the numbers 0-9\n")
				guessString = input("Guess a 3 digit number with no spaces in between numbers and no repeats: ")
				print()
			
			#makes sure guess is 3 digits long
			while len(guessString) != 3:
				print("please make a guess only 3 digits in length\n")
				guessString = input("Guess a 3 digit number with no spaces in between numbers and no repeats: ")
				print()

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
		print(response,"\n")
	print("Congradulations, you guessed the correct number!")

def PicoFermi(guess):

	guess[0], guess[1] = guess[1], guess[0] #try swapping first two numbers
	print(guess)
	answer = input("Please input response \n")
	print()

	if answer != "Fermi Fermi":
		guess[0], guess[1] = guess[1], guess[0] #if that doesn't work swap back try next swap
		guess[0], guess[2] = guess[2], guess[0]
		print(guess)
		answer = input("Please input response \n")
		print()

		if answer != "Fermi Fermi":
			guess[0], guess[2] = guess[2], guess[0] #if that didn't work swamp back try next swamp
			guess[1], guess[2] = guess[2], guess[1]


	return guess, answer

def FermiFermi(guess):
	global FermiIndex
	temp = guess[FermiIndex]



	guess[FermiIndex] = digits[0]
	digits.remove(guess[FermiIndex])
	print(guess)
	answer = input("Please input response \n")
	print()
	
	if answer == "Pico Fermi":
		lastDigit = guess[FermiIndex]
		guess[FermiIndex] = temp
		temp = guess[FermiIndex]
		FermiIndex += 1
		temp = guess[FermiIndex]
		guess[FermiIndex] = lastDigit
		print(guess)
		answer = input("Please input response \n")
		print()

		if answer != "Fermi Fermi Fermi":
			guess[FermiIndex] = temp
			FermiIndex += 1
			guess[FermiIndex] = lastDigit
			print(guess)
			answer = input("Please input response \n")
			print()


	if answer == "Fermi":
		guess[FermiIndex] = temp
		FermiIndex += 1
		temp = guess[FermiIndex]
		guess[FermiIndex] = digits[0]
		digits.remove(guess[FermiIndex])
		print(guess)
		answer = input("Please input response\n")
		print()


		if answer == "Fermi":
			guess[FermiIndex] = temp
			FermiIndex += 1
			guess[FermiIndex] = digits[0]
			digits.remove(guess[FermiIndex])
			print(guess)
			answer = input("Please input response\n")
			print()


	return guess, answer



def TriplePico(guess): #if guess by computer is responded by pico pico pico
	 #from here computer will guess different combinations till it wins
	guess[0], guess[1], guess[2] = guess[1], guess[2], guess[0]
	print(guess)
	answer = input("Please input response \n")
	print()

	if answer != "Fermi Fermi Fermi":
		guess[0], guess[1], guess[2] = guess[1], guess[2], guess[0]
		print(guess)
		answer = input("Please input response \n")
		print()
		

	return guess, answer

def PicoPicoFermi(guess):
	guess[0], guess[2] = guess[2], guess[0]
	print(guess)
	answer = input("Please input response \n")
	print()
	if answer == "Pico Pico Pico":
		guess[0], guess[1], guess[2] = guess[1], guess[2], guess[0]
		print(guess)
		answer = input("Please input response \n")
		print()

		if answer == "Pico Pico Pico":
			guess[0], guess[1], guess[2] = guess[1], guess[2], guess[0]



	return guess, answer

def creating():

	print("The computer will make a guess then you will input the correct response \
if you input fermi fermi fermi, then the guess is correct and the game will be over. \
When responding ensure that Pico's are written before Fermis, and write your response with the words \
Fermi Pico Bagel, seperating the words by spaces and capitalizing words\n")

	#first guess by computer will be random
	guess = generateNum()
	print(guess)
	answer = input("Please input response: \n")	
	print()
	while answer != "Fermi Fermi Fermi":
		
		if answer == "Bagel":
			guess = generateNum()
			print(guess)
			answer = input("Please input response: \n")	
			print()

		if answer == "Pico Fermi":
			guess, answer = PicoFermi(guess)
			
		if answer == "Fermi Fermi":
			guess, answer = FermiFermi(guess)

		elif answer == "Pico Pico Pico": 
			guess, answer = TriplePico(guess)

		elif answer == "Pico Pico Fermi":
			guess, answer = PicoPicoFermi(guess)



		elif answer == "Fermi Fermi Fermi":
			pass

		else:
			print("Please ensure you are only inputing Pico, Bagel, or Fermi, as a response seperated by spaces and capitalized")
			answer = input("Please input response: \n")
			print()



	print("Game over, the computer has guessed your number")

def main():
	#Rules()
	gamemode = startGame()
	if gamemode == "Guessing":
		test = generateNum()
		guessing(test)
	if gamemode == "Creating":
		creating()

if __name__ == "__main__":
	main()
