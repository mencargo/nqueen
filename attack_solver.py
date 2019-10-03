#!/usr/bin/env python3
import time
import copy
import sys

print("Usage: python3 attack_solver.py [max_size] [min_size] [log_level]")
print("max_size  : Board maximum size, default = 10")
print("min_size  : Board initial size, default = 1")
print("log_level : Output detail shown in the process, default = 0")
print("            Recommended only whith min_size = max_size")
print("            0 Only show statistics")
print("            1 Display all solutions with boards")
print("            2 Display all steps in the process showing queen boards")
print("            3 Display all steps in the process showing attack maps")
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

def newMove(a, x, y, move):
	# same row
	for i in range(n):
		a[i][y] += move

	# same column
	for j in range(n):
		a[x][j] += move

	# up left diagonal
	for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
		a[i][j] += move

	# up right diagonal
	for i, j in zip(range(x, -1, -1), range(y, n)):
		a[i][j] += move

	# down left diagonal
	for i, j in zip(range(x, n), range(y, -1, -1)):
		a[i][j] += move

	# down right diagonal
	for i, j in zip(range(x, n), range(y, n)):
		a[i][j] += move

	return True

def newSolution(b):
	global s
	s.append(copy.deepcopy(b))
	if log > 0:
		pBoard(b)

def solve(b, a, x, n):
	if x >= n:
		return

	for y in range(n):
		if a[x][y] == 0:
			newMove(a, x, y, 1)
			b[x][y] = 1
			if x == n - 1:
				newSolution(b)
				b[x][y] = 0
				newMove(a, x, y, -1)
			else:
				if log == 2:
					pBoard(b)
				elif log == 3:
					pBoard(a)
				solve(b, a, x + 1, n)
				b[x][y] = 0
				newMove(a, x, y, -1)


for n in range(min, max):
	s = [] # Solutions
	queens = [[0] * n for _ in range(n)] # Queens Board
	attack = [[0] * n for _ in range(n)] # Attack Board Map
	start = time.time()
	print("N =", n, end = '| ')
	solve(queens, attack, 0, n)
	print(len(s), "solutions found in", '{0:.5f}'.format(time.time() - start), "seconds")