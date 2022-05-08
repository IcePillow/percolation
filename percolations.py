### IMPORTS ###
import os
import numpy as np
from time import sleep
import random

### CONSTANTS ###
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


### UTILITY METHODS ###

'''
Draws a board. Expects a matrix of size nxn.
'''
def drawTileBoard(board):
	n = len(board)

	print("\u2588"*(n+2))
	for row in board:
		print("\u2588", end="")
		for i in row:
			if i==0:
				print("\u2591", end="")
			elif i==9:
				print("X", end="")
			else:
				print("O", end="")
		print("\u2588")
	print("\u2588"*(n+2))

'''
Gets input from the user. Case insensitive.
'''
def getInput():
	print("> ", end="")
	return str.lower(input())

'''
Utility method for visualConnected()
'''
def displayVisualConnected(matrix):
	n = len(matrix)

	os.system('cls' if os.name == 'nt' else 'clear')
	print("\u2588"*(n+2))

	#loop over grid
	for i in range(0, len(matrix)):
		print("\u2588", end="")
		for j in range(0, len(matrix)):
			value = int(matrix[i][j])

			if value == -1:
				print(" ", end="")
			elif value == 0:
				print("\u2591", end="")
			else:
				print(symbols[(value-1) % len(symbols)], end="")
		print("\u2588")

	print("\u2588"*(n+2))

'''
Determines if a board is connected from top to bottom.
	board - the matrix
	sleepTime - time to wait
	visual - boolean, whether or not to display
Returns, a list with
	- boolean of whether or not it was connected
	- matrix with a board that represents the finished algorithm
'''
def testConnected(board, sleepTime, visual):
	#board details
	n = len(board)
	matrix = np.full((n, n), -1)

	#the next integer value
	sym = 1

	#loop through the values
	for i in range(0, n):
		for j in range(0, n):

			#if this slot is a wall
			if board[i][j] == 0:
				matrix[i][j] = 0
			#connect to something above
			elif i > 0 and board[i-1][j] != 0:
				matrix[i][j] = matrix[i-1][j]

				#fix things connected to the left
				if j > 0 and board[i][j-1] != 0:
					for k in range(0, i+1):
						for l in range(0, j):
							if matrix[k][l] == matrix[i][j-1]:
								matrix[k][l] = matrix[i][j]
			#connect to something left
			elif j > 0 and board[i][j-1] != 0:
				matrix[i][j] = matrix[i][j-1]
			#if this slot is an unconnected path
			else:
				matrix[i][j] = sym
				sym += 1

			#display
			if visual:
				displayVisualConnected(matrix)

			#wait for loop
			sleep(sleepTime)

	#check if completed
	topEntries = []
	for col in range(0, n):
		if (matrix[0][col] != 0) and (not matrix[0][col] in topEntries):
			topEntries.append(matrix[0][col])
	successful = 0
	for col in range(0, n):
		if matrix[n-1][col] in topEntries:
			successful = matrix[n-1][col]
			break


	#redraw the board to match successful
	for i in range(0, n):
		for j in range(0, n):
			if matrix[i][j] != 0 and matrix[i][j] != successful:
				matrix[i][j] = 1
			elif matrix[i][j] != 0:
				matrix[i][j] = 9

	return [successful != 0, matrix]


### PRIMARY METHODS ###

'''
Runs a board simulation and calculates whether or not
display - boolean of whether or not to show alg animation
'''
def runBoard(display):
	#get parameters from user
	size = ""
	while True:
		print("What size board? (1-30)")
		size = getInput()
		if size.isnumeric() and int(size) >= 1 and int(size) <= 30:
			size = int(size)
			break
		else:
			print("Invalid board size")

	prob = ""
	while True:
		print("What probability value? (1-100)")
		prob = getInput()
		if prob.isnumeric():
			prob = int(prob)
			break
		else:
			print("Invalid probability")

	#create board
	board = np.zeros((size, size))
	for i in range(0, size):
		for j in range(0, size):

			r = random.randint(1, 100)
			if r <= prob:
				board[i][j] = 1

	# draw and calculate
	if display:
		result = testConnected(board, 0.03, True)
		if result[0] == True:
			print("\nBoard is connected:")
		else:
			print("\nBoard is not connected:")
		drawTileBoard(result[1])
	else:
		drawTileBoard(board)


### MAIN ###

def main():
	print("Welcome to percolations.\n")

	#main loop
	while True:
		#show options and get input
		print("What would you like to do?\
			\n    simulate - same as board but displays algorithm\
			\n    board - calculate for a single board\
			\n    exit - exit the program")
		string = getInput()

		#check input
		if string == "exit":
			print("Goodbye.")
			break
		elif string == "simulate":
			runBoard(True)
		elif string == "board":
			runBoard(False)
		else:
			print("Unrecognized input, please try again.")

		#prepare for next loop
		print("\n\n----------------------------------------\n\n")



if __name__ == "__main__":
    main ()