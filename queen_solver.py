#!/usr/bin/env python3
import time
import copy
import sys

print("Usage: python3 queen_solver.py [max_size] [min_size] [log_level]")
print("max_size  : Board maximum size, default = 10")
print("min_size  : Board initial size, default = 1")
print("log_level : Output detail shown in the process, default = 0")
print("            Recommended only whith min_size = max_size")
print("            0 Only show statistics")
print("            1 Display all solutions with boards")
print("            2 Display all steps in the process")
print()
log = 0
min = 1
max = 11

if len(sys.argv) >= 2 and str.isdigit(sys.argv[1]):
	max = int(sys.argv[1]) + 1
if len(sys.argv) >= 3 and str.isdigit(sys.argv[2]):
	min = int(sys.argv[2])
if len(sys.argv) >= 4 and str.isdigit(sys.argv[3]):
	log = int(sys.argv[3])

def pBoard(b):
	print()
	for x in range(n):
		print('{:>2}'.format(n-x), end = '| ')
		for y in range(n):
			print(b[x][y], end = ' ')
		print()
	return

def isFree(b, x, y):
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
	if log > 0:
		pBoard(b)

def solve(b, x, n):
	if x >= n:
		return

	for y in range(n):
		if isFree(b, x, y):
			b[x][y] = 1
			if x == n - 1:
				newSolution(b)
				b[x][y] = 0
			else:
				if log == 2:
					pBoard(b)
				solve(b, x + 1, n)
				b[x][y] = 0

for n in range(min, max):
	s = [] # Solutions
	queens = [[0] * n for _ in range(n)] # Queens Board
	start = time.time()
	print("N =", n, end = '| ')
	solve(queens, 0, n)
	print(len(s), "solutions found in", '{0:.5f}'.format(time.time() - start), "seconds")
