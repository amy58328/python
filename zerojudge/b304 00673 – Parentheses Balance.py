# b304: 00673 – Parentheses Balance

N = int(input())

for i in range(N):
	str = input()
	lis = []

	for c in str:
		if c == '(' or c == '[':
			lis.append(c)

		elif lis:
			if lis.pop() == '(':
				if c != ')':
					print('No')
					break
			else:
				if c != ']':
					print('No')
					break
		else:
			print("No")
			break;
	else:
		if lis:
			print('No')
		else:
			print('Yes')
