n = int(input())
queue = []

while n>0 :
	str = input()

	if str[0] == '1':
		num = int(str.split(' ')[1])
		queue.append(num)

	elif str[0] == '2':
		if len(queue) != 0:
			print(queue[0])
		else:
			print("-1")
	else:
		if len(queue) != 0:
			queue.pop(0)

	n-=1