#!/usr/bin/env python3
import sys

n = 4 # Board Size
q = [] # Queen Solutions
t = [] # Temp


# print("Usage: python3 index.py [N]")

# if len(sys.argv) != 2:
# 	print("Size unspecified")
# elif str.isdigit(sys.argv[1]): # includes 0
# 	n = int(sys.argv[1])
# else:
# 	print("N should be a positive integer")

print("Solving for", n)

b = [0]*n*n

q = b

print()
for x in range(n):
	for y in range(n):
		print(b[x*n+y], end = ' ')
		if y == (n-1):
			print()
		# if q[x][y] == 0 and b[x][y] == 0:
		# 	q[x][y] = 1
		# 	b[x]

	