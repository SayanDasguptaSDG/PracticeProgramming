from collections import deque

stack = deque()
s = "(()())(()())())("
l = len(s)
top = 0

for i in range(l):
	if s[i] != ")":
		stack.append(s[i])
		print(stack)
		print("Top: " + str(top))
		top += 1
	else:
		try:
			top -= 1
			print("Popping: " + stack.pop())
			print(stack)
			print("Top: " + str(top))
		except:
			print("IndexError: pop from an empty deque")
			print("Balancing parentheses cannot proceed any further. Exit mode activated.")
			exit(0)
if top > 0:
	print("Top: " + str(top) + " greater than 0.\nHence, parentheses are not balanced.")
else:
	print("Balanced parentheses is achieved.")
