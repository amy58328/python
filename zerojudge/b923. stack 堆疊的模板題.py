n = int(input())
stack = []

while n>0 :
	str = input()

	if str[0] == '3':
		num = int(str.split(' ')[1])
		stack.append(num)

	elif str[0] == '2':
		if len(stack) 	!= 0:
			print(stack[-1]) ## 輸出最後一個數字
	else:
		if len(stack) != 0:
			stack.pop()

	n-=1