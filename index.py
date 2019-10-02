#!/usr/bin/env python3

n = 4 # Board Size
q = [] # Queen Solutions
b = [[0] * n for _ in range(n)] # Temp board

print("Solving for", n)

def pBoard(b):
	print()
	for x in range(n):
		print('{:>2}'.format(n-x), end = '| ')
		for y in range(n):
			print(b[x][y], end = ' ')
			if y == (n-1):
				print()
	return True

def isFree(b,x,y):
	# same row
	for i in range(x):
		if b[i][y] == 1:
			return False

	# same column
	for i in range(y):
		if b[x][i] == 1:
			return False

	# up left diagonal
	for i,j in zip(range(x, -1, -1), range(y, -1, -1)): 
		if b[i][j] == 1: 
			return False

	# up right diagonal
	for i,j in zip(range(x, -1, -1), range(y, n)): 
		if b[i][j] == 1: 
			return False

	return True

for x in range(n):
	for y in range(n):
		if isFree(b,x,y):
			b[x][y] = 1
			pBoard(b)
			# continue

