#!/usr/bin/env python3
import time
import copy
import sys

def pBoard(b):
	print()
	for x in range(n):
		print('{:>2}'.format(n-x), end = '| ')
		for y in range(n):
			print(b[x][y], end = ' ')
		print()
	return

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
	for i, j in zip(range(x, -1, -1), range(y, -1, -1)): 
		if b[i][j] == 1: 
			return False

	# up right diagonal
	for i, j in zip(range(x, -1, -1), range(y, n)): 
		if b[i][j] == 1: 
			return False

	return True

def newSolution(b):
	global s
	s.append(copy.deepcopy(b))

def solve(b,x,n):
	if x >= n:
		return

	for y in range(n):
		if isFree(b, x, y):
			b[x][y] = 1
			if x == n - 1:
				newSolution(b)
				# pBoard(b)
				b[x][y] = 0

			solve(b, x + 1, n)
			b[x][y] = 0


for n in range(13):
	s = [] # Solutions
	b = [[0] * n for _ in range(n)]
	start = time.time()
	print("N =", n, end = '| ')
	solve(b, 0, n)
	print(len(s), "solutions found in", '{0:.5f}'.format(time.time() - start), "seconds")