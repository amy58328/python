# uva 11995 - I Can Guess the Data Structure!

def FS(op,num):
	stack = []

	for i in range(len(op)):
		if op[i] == 1:
			stack.append(num[i])

		else:
			if len(stack) == 0 :
				return False

			top = stack[-1]
			if num[i] != top :
				return False
			else :
				stack.pop()
	return True

def FQ(op,num):
	Queue = []

	for i in range(len(op)):
		if op[i] == 1:
			Queue.append(num[i])

		else:
			if len(Queue) == 0 :
				return False

			top = Queue[0]
			if num[i] != top :
				return False
			else :
				Queue.pop(0)
	return True

def FP(op,num):
	priority = []

	for i in range(len(op)):
		if op[i] == 1:
			priority.append(num[i])

		else:
			if len(priority) == 0 :
				return False

			priority.sort()
			top = priority[-1]

			if num[i] != top :
				return False
			else :
				priority.pop()
	return True


def main():
	while True:
		try:
			N = int(input())

			op = []
			num = []
			# 獲得指令跟數字
			for i in range(N):
				str = input()
				op.append(int(str.split()[0]))
				num.append(int(str.split()[1]))

			# 判斷stack Queue Priority Queue
			stack = FS(op,num)
			Queue = FQ(op,num)
			Priority = FP(op,num)

			if stack == True and Queue == False  and Priority == False:
				print("stack")
			elif stack == False and Queue == True  and Priority == False:
				print("queue")
			elif stack == False and Queue == False  and Priority == True:
				print("priority queue")
			elif stack == False and Queue == False  and Priority == False:
				print("impossible")
			else:
				print("not sure")

		except:
			break;
main()
